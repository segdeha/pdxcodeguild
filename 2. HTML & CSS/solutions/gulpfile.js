var gulp         = require( 'gulp' )
var gutil        = require( 'gulp-util' )
var sass         = require( 'gulp-sass' )
var autoprefixer = require( 'gulp-autoprefixer' )

gulp.task( 'default', [ 'sass', 'watch' ])

// compile scss
// concat vendor css with my compiled css
// move to dist/assets/styles.css
gulp.task( 'sass', function( file ) {
    if ( !file.path ) {
        return
    }
    const dest = file.path.replace('.scss', '.css')
	gulp.src( file.path )
		.pipe( sass() )
			.on( 'error', gutil.log )
		.pipe( autoprefixer({ browsers : [ 'Safari 5' ] }) )
		.pipe( gulp.dest( dest ) )
})

// watch for changes and recompile automatically
gulp.task( 'watch', function() {
	gulp
		.watch( '**/*.scss', [ 'sass' ] )
		.on( 'change', function( event ) {
			gutil.log( 'File ' + event.path + ' was ' + event.type + ', running tasks...' )
		})
})
