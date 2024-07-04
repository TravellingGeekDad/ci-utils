import git_changelog.build as build
import git_changelog.versioning as versioning

# Create a changelog object to determine versions
changes = build.Changelog(
    repository='.',
    convention="angular",
    provider="gitlab",
    parse_trailers=True,
    sections=("build", "deps", "feat", "fix", "refactor"),
    versioning="semver",
    bump="auto",
    zerover=True
)

# Get our next version
next_version = changes.versions_list[0].planned_tag

if next_version == None:
    # If we don't have one, start at 0.1.0
    print('0.1.0')
else:
    # Otherwise, get just the version string to pass to Hatch
    print(versioning.version_prefix(next_version)[0])