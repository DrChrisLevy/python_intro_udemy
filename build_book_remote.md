# Build Book Locally

```

jupyter-book build book/

```

# Update Book Github Pages

After building the book, commit and push the changes i.e.


```

git add book/*
git commit -m 'Chapter 7 work'
git push

```

Then update the github pages branch.

```

ghp-import -n -p -f book/_build/html/

```