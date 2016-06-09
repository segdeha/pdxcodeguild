# Gulp

Gulp is a system that allows you to automate repetitive tasks. We are going to use it to compile our [Sass](http://sass-lang.com/) files automagically whenever we make changes to them.

To do that, we’re going to need the following packages:

- [gulp](https://www.npmjs.com/package/gulp)
- [gulp-util](https://www.npmjs.com/package/gulp-util)
- [gulp-watch](https://www.npmjs.com/package/gulp-watch)
- [gulp-sass](https://www.npmjs.com/package/gulp-sass)
- [gulp-autoprefixer](https://www.npmjs.com/package/gulp-autoprefixer)

------

## Install Packages

1. `cd` into the directory where you will be working on HTML/CSS assignments
1. Run `npm init`, use the default values for all fields (i.e. just keep pressing [enter] until it finishes)
1. From a terminal window, run the following commands:

```
npm install --save-dev gulp
npm install --save-dev gulp-util
npm install --save-dev gulp-watch
npm install --save-dev gulp-sass
npm install --save-dev gulp-autoprefixer
```

Let me know if you have trouble with this. We’re going to depend heavily on these tools!

------

## Install Gulp File

Gulp needs a file (usually named `gulpfile.js`) to tell it exactly what to do when it’s run. For now, you can download this [gulpfile.js](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/2.%20HTML%20%26%20CSS/solutions/gulpfile.js?token=AAAQ0kG4t523ux6A5qOuyRM35aVe8EzYks5XYt8awA%3D%3D) to the same directory where you ran the `npm` commands above.

------

## Verify Gulp is Working

Let’s make sure we have everything wired up correctly.

1. `cd` into the same directory as your `gulpfile.js`
1. In that directory, create a new directory called `sass`, and inside that directory create new directories called `src` and `dest`
1. Into `sass/src`, download [example.scss](https://raw.githubusercontent.com/segdeha/pdxcodeguild/master/2.%20HTML%20%26%20CSS/solutions/sass/src/example.scss?token=AAAQ0oBYKvxZ9LacmkqxoqzK9Kg7LSNcks5XYuAIwA%3D%3D)
1. From the same directory as your `gulpfile.js`, run `gulp`
1. Look in `sass/dest`; you should see a new file called `example.css`; open the file and observe that there is a `color` attribute set to `red`
1. In `sass/src/example.scss`, change `red` to `blue` for the value of the `$color` variable
1. Look again at `sass/dest/example.css` to make sure the value of the `color` attribute is now `blue`

If all of the above worked, you’re all set! If not, let me know and we’ll troubleshoot together.
