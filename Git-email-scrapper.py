import requests

# Function to fetch repository data from GitHub
def get_repositories(user_id):
    url = f"https://api.github.com/users/{user_id}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repos = response.json()
        if not repos:
            print("No repositories found.")
            return []
        print(f"Repositories for user {user_id}:")
        for i, repo in enumerate(repos, 1):
            repo_name = repo['name']
            repo_type = "Forked" if repo['fork'] else "Owned"
            print(f"{i}. {repo_name} ({repo_type})")
        return repos
    else:
        print(f"Failed to fetch repositories. Status code: {response.status_code}")
        return []

# Function to fetch commits of a specific repository
def get_commits(user_id, repo_name):
    url = f"https://api.github.com/repos/{user_id}/{repo_name}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        if not commits:
            print("No commits found.")
        else:
            return commits
    else:
        print(f"Failed to retrieve commits. Status code: {response.status_code}")
        return []

# Function to fetch patch data from a commit patch URL
def fetch_patch_data(patch_url):
    try:
        # Fetch the patch content using requests
        response = requests.get(patch_url)
        response.raise_for_status()  # Check for request errors
        return response.text

    except requests.exceptions.RequestException as e:
        print(f"Error fetching patch: {e}")
        return None

# Function to extract the keyword from patch content
def extract_keyword_from_patch(patch_content, keyword="From:"):
    keyword_values = set()  # Use a set to store unique values of the keyword

    for line in patch_content.splitlines():
        if keyword in line:
            keyword_values.add(line.strip())  # Add the line to the set

    return keyword_values

# Function to process commits and print results for a given mode
def process_commits(user_id, repo_name, mode="detailed"):
    commits = get_commits(user_id, repo_name)

    if commits:
        all_keyword_values = set()

        if mode == "flash":
            # In Flash mode, we only process the first commit
            commit = commits[0]
            commit_patch_url = f"https://github.com/{user_id}/{repo_name}/commit/{commit['sha']}.patch"
            
            patch_content = fetch_patch_data(commit_patch_url)
            if patch_content:
                keyword_values = extract_keyword_from_patch(patch_content)
                all_keyword_values.update(keyword_values)

        elif mode == "detailed":
            # In Detailed mode, process all commits
            for commit in commits:
                commit_patch_url = f"https://github.com/{user_id}/{repo_name}/commit/{commit['sha']}.patch"
                
                patch_content = fetch_patch_data(commit_patch_url)
                if patch_content:
                    keyword_values = extract_keyword_from_patch(patch_content)
                    all_keyword_values.update(keyword_values)

        # Display only the unique keyword values found across all commits
        if all_keyword_values:
            print("\nUnique emails Found:")
            for value in all_keyword_values:
                print(value)
        else:
            print(f"\nNo emails found.")
    else:
        print("No commits found in the selected repository.")

# Main function to orchestrate the flow
def main():
    user_id = input("Enter GitHub username: ")
    
    # Get list of repositories
    repos = get_repositories(user_id)
    
    if repos:
        # Let the user select a repository
        try:
            repo_choice = int(input(f"\nSelect a repository (1-{len(repos)}): "))
            if 1 <= repo_choice <= len(repos):
                selected_repo = repos[repo_choice - 1]['name']
                
                # Let the user choose a mode using 1 or 2
                print("\nSelect mode:")
                print("1. Flash mode (process first commit only)")
                print("2. Detailed mode (process all commits)")
                
                mode_choice = input("Enter 1 for Flash or 2 for Detailed: ").strip()
                
                # Map choice 1 to 'flash' and 2 to 'detailed'
                if mode_choice == "1":
                    mode = "flash"
                elif mode_choice == "2":
                    mode = "detailed"
                else:
                    print("Invalid choice. Defaulting to 'flash' mode.")
                    mode = "flash"

                # Process commits based on selected mode
                process_commits(user_id, selected_repo, mode)

            else:
                print("Invalid repository choice.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
