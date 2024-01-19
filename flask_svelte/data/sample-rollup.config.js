import { spawn } from 'child_process';
import svelte from 'rollup-plugin-svelte';
import commonjs from '@rollup/plugin-commonjs';
import terser from '@rollup/plugin-terser';
import resolve from '@rollup/plugin-node-resolve';
import livereload from 'rollup-plugin-livereload';
import css from 'rollup-plugin-css-only';
import sveltePreprocess from 'svelte-preprocess';
import tailwindcss from 'tailwindcss';
import autoprefixer from 'autoprefixer';
import watchGlobs from 'rollup-plugin-watch-globs';

const production = !process.env.ROLLUP_WATCH;

function serve() {
	let server;

	function toExit() {
		if (server) server.kill(0);
	}

	return {
		writeBundle() {
			if (server) return;
			server = spawn('flask', ['run', '--debug'], {
				stdio: ['ignore', 'inherit', 'inherit'],
				shell: true
			});

			process.on('SIGTERM', toExit);
			process.on('exit', toExit);
		}
	};
}

function rollupPlugins(index) {
	let plugins = [
		svelte({
			compilerOptions: {
				// enable run-time checks when not in production
				dev: !production
			},
			preprocess: sveltePreprocess({
				postcss: {
					plugins: [
						tailwindcss(),
						autoprefixer,
					]
				}
			})
		}),
		// we'll extract any component CSS out into
		// a separate file - better for performance
		css({ output: 'style.css' }),

		// If you have external dependencies installed from
		// npm, you'll most likely need these plugins. In
		// some cases you'll need additional configuration -
		// consult the documentation for details:
		// https://github.com/rollup/plugins/tree/master/packages/commonjs
		resolve({
			browser: true,
			dedupe: ['svelte'],
			exportConditions: ['svelte']
		}),
		commonjs(),

		// Watch the `public` directory and refresh the
		// browser on changes when not in production
		!production && livereload('app/'),

		// If we're building for production (npm run build
		// instead of npm run dev), minify
		production && terser()
	]

	if (index === 0 && !production) {
		plugins.push([serve(), watchGlobs(['./rollup.config.js', './tailwind.config.js'])]);
	}
	return plugins;
}

let svelte_apps = [];

export default svelte_apps.map((name, index) => ({
	input: `app/svelte/${name}/main.js`,
	output: {
		sourcemap: true,
		format: 'iife',
		name: name + 'App',
		file: `app/static/svelte/${name}/index.js`
	},
	plugins: rollupPlugins(index),
	watch: {
		clearScreen: false
	}
}));

