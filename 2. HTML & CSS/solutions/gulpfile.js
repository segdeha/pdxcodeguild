var gulp         = require( 'gulp' )
var gutil        = require( 'gulp-util' )
var sass         = require( 'gulp-sass' )
var autoprefixer = require( 'gulp-autoprefixer' )

gulp.task( 'default', [ 'sass', 'watch' ])

const config = {
    src: 'sass/src/*.scss',
    dest: 'sass/dest/'
}

// compile scss, save in the same directory with the extension `.css`
gulp.task( 'sass', function() {
	gulp.src( config.src )
		.pipe( sass() )
			.on( 'error', gutil.log )
		.pipe( autoprefixer({ browsers : [ 'Safari 5' ] }) )
            .on( 'error', gutil.log )
		.pipe( gulp.dest( config.dest ) )
            .on( 'error', gutil.log )
})

// watch for changes and recompile automatically
gulp.task( 'watch', function() {
	gulp
		.watch( config.src, [ 'sass' ] )
		.on( 'change', function( event ) {
			gutil.log( 'File ' + event.path + ' was ' + event.type + ', running tasks...' )
		})
})
