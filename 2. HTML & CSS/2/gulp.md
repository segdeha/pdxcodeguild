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

Gulp needs a file (usually named `gulpfile.js`) to tell it exactly what to do when it’s run. For now, you can download this [gulpfile.js]() to the same directory where you ran the `npm` commands above.

