# Pull Request Label


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![License: MIT](https://img.shields.io/github/license/migantoju/pull-request-label)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/migantoju)
[![release !](https://img.shields.io/github/v/release/migantoju/pull-request-label)](https://github.com/migantoju/pull-request-label/releases/tag/v1.0)

# ℹ️ Overview

This is a github action that applies a label to the pull requests where you use this actions,
The label is a text that gives visibility to the people who maintain the project or own the project, about a pull request with a feature, solving a bug, etc.
In this way, it is possible to give greater visibility to those responsible and maintain a cleaner process.

# 🚀 How to use
First of all, you need to create some dirs in your project `.giithub/workflows`, inside create a `yml` file
the name for example `labeler.yml`. Once you have this, it's time to write the following.

```yaml
name: "Label Pull Request"
on: [pull_request]

jobs:
  test_job:
    runs-on: ubuntu-latest
    steps:
      - name: Set Label
        uses: migantoju/pull-request-label@v1.0
        with:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          PR_NUMBER: ${{ github.event.number }}

```

And that's all, only you need to make some pull requests with changes and magically, this
will set a label with the `SIZE/*`.

# Extra
If for some reason, the labeler doesn't work, then change the `uses` line in the `labeler.yml`.
```yaml

# from this 
uses: migantoju/pull-request-label@v1.0

# to this
uses: migantoju/pull-request-label@master
```

# ⚖️ LICENSE

[MIT](https://github.com/migantoju/pull-request-label/blob/master/LICENSE)

Maded with ❤️.
