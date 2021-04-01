# Learning Equality Website project conventions

## Git branching model

We follow a loose version of the [Git flow branching model](https://nvie.com/posts/a-successful-git-branching-model/).

- Make pull requests against: `master`
- The release prep branch is: `master`
- The client QA branch is: `staging`
- The internal QA branch is: `develop`
- Do not treat the following branches as merge sources: `develop`, `staging`

1. Make changes on a new branch, including a broad category and the ticket number if relevant e.g. `feature/123-extra-squiggles`, `fix/newsletter-signup`.
2. Push your branch to the remote.
3. Make merge requests at https://github.com/learningequality/learningequality.org-v2
4. Edit details as necessary.

If you need to preview work on `staging`, this can be merged and deployed manually without making a merge request. You can still make the merge request as above, but add a note to say that this is on `staging`, and not yet ready to be merged to `master`.

## Deployment Cycle

<!-- #FIXME Developer, delete this once you have reviewed this file.
Choose a deployment approach below, and delete what you don't need.
-->

<!-- Option one, simple deployment cycle

### Simple flavour

Make sure `master` contains all the desired changes (and is pushed to the remote repository and has passed CI). Deploy to production (see [deployment documentation](deployment.md)).

-->

<!-- Option two, release-based deployment cycle

### Versioned releases

This requires a 'release' QA server running a `release-x.x.x` branch which can be considered to be a merge source.

1. Make merge requests to the branch `release-x.x.x`.
1. Add a heading `# x.x.x (yyyy-mm-dd)` to `CHANGELOG.md`, detailing what is in this release.
1. Merge `release-x.x.x` to `master`.
1. Deploy to production (see [deployment documentation](deployment.md)).
1. Tag the merge commit
    1. `git tag x.x.x`
    1. `git push --tags`
1. Create a new branch `release-x.x+1.x`, or `release-x+1.x.x` as appropriate, from `master`.

Add release notes to (docs/release-notes.md).

#### Deploying bug fixes

Urgent bug fixes should be made against the latest-deployed release, i.e. x.x.x. There is possibly already a `release-x.(x+1).x` branch in progress.

1. Pull `master`.
1. Create the bug fix branch, e.g. `hotfix/mend-squiggles`.
    1. In `CHANGELOG.md`, add a new section to `x.x.(x+1) (yyyy-mm-dd)` where
       the date is the release date.
1. If it needs client approval, or to be user-tested, deploy to staging.
1. Make a merge request from `hotfix/mend-squiggles` to `master`.
1. Once the change is approved, accept the merge request, and deploy to Production
1. Tag the merge commit
    1. `git tag x.x.(x+1)`
    1. `git push --tags`
1. Merge master into `release-(x+1).x.x`.
-->
