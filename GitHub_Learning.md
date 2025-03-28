

## What is the purpose of GitHub?
GitHub is a cloud-based platform for version control and collaboration using Git. It allows developers to store, manage, and track code changes while working together on projects. It is widely used for open-source contributions, team collaborations, and project management.

## What are branches and why are they useful?
Branches in GitHub allow developers to create separate versions of a codebase for development, testing, or new features. They help in:
- Working on new features without affecting the main code.
- Fixing bugs in an isolated environment.
- Collaborating with multiple developers without conflicts.
- Merging changes back into the main branch when complete.

## What is a pull request and how does it work?
A **pull request (PR)** is a way to propose and review changes before merging them into the main branch. The process involves:
1. Creating a new branch and making changes.
2. Pushing the changes to GitHub.
3. Opening a pull request to compare changes with the main branch.
4. Team members review, provide feedback, and approve changes.
5. Once approved, the changes are merged into the main branch.

## How do you resolve merge conflicts?
Merge conflicts occur when multiple changes affect the same lines of code. To resolve them:
1. Identify conflicting files using `git status`.
2. Open the conflicting file and manually edit sections marked with `<<<<<<<`, `=======`, and `>>>>>>>`.
3. Decide which changes to keep and remove conflict markers.
4. Stage the resolved file using `git add <file>`.
5. Commit the resolution with `git commit -m "Resolved merge conflict"`.

## How would you collaborate with a team using GitHub?
Collaboration on GitHub typically follows these steps:
1. **Clone the repository**: Each team member clones the repo using `git clone <repo_url>`.
2. **Create a new branch**: Work on features separately using `git checkout -b feature-branch`.
3. **Make changes and commit**: Modify files and commit using `git add .` and `git commit -m "Commit message"`.
4. **Push to GitHub**: Upload changes using `git push origin feature-branch`.
5. **Open a pull request**: Submit a PR for review and feedback.
6. **Merge changes**: Once approved, merge changes into the main branch.
7. **Pull updates**: Regularly sync with the main branch using `git pull origin main` to avoid conflicts.

GitHub also provides **issues**, **projects**, and **discussions** for team collaboration and tracking progress.
