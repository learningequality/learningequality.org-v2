# Front end tooling

This set of tooling should form the basis for any new wagtail projects. It can also be used for custom django builds: copy the `static_src` directory from here to your build. And various config files from the project root too.

## What's required

To install node on the host machine we recommend using [`nvm`](https://github.com/creationix/nvm). Once you have `nvm` installed simply run `nvm install` to install and activate the version of node required for the project. Refer to the [`nvm` documentation](https://github.com/creationix/nvm#usage) for more details about available commands.

## Setting up a new project from the wagtail-kit tooling

The wagtail-kit tooling is versioned via `package.json`, and the `package-lock.json` lockfile pins all of the project’s direct and transitive dependencies. If you wish to start the project with up to date dependencies without doing manual upgrades, you can discard the lockfile and re-create it:

```sh
rm -rf node_modules
rm package-lock.json
npm install
```

Remember to then commit the updated `package-lock.json`.

## What's included

- [Sass](http://sass-lang.com/) CSS with [auto-prefixing](https://github.com/postcss/autoprefixer).
- [Babel](https://babeljs.io) for ES2015+ support.
- [Browsersync](https://www.browsersync.io) for autoreloading.
- [Webpack](https://webpack.js.org/) for module bundling.
  - With `babel-loader` to process JavaScript.
  - With `css-loader`, `postcss-loader`, and `sass-loader` to process stylesheets.
- Consideration for images, currently copying the directory only - to avoid slowdowns and non-essential dependancies. We encourage using SVG for UI vectors and pre-optimised UI photograph assets.
- [Build commands](#build-scripts) for generating testable or deployable assets only
- CSS linting with `stylelint`
- JS linting with `eslint`
- [Jest](https://jestjs.io/) for JavaScript unit tests.
- React support

## Developing with it

- To start the development environment, follow instruction in README.md in the project root
- Source files for developing your project are in `static_src` and the distribution folder for the compiled assets is `static_compiled`. Don't make direct changes to the `static_compiled` directory as they will be overwritten.

## Tests

JavaScript unit tests for this project use [Jest](https://jestjs.io/). Here are commands you can use:

```sh
# Run the whole test suite once.
npm run test
# Run the whole test suite, collecting test coverage information.
npm run test:coverage
# Start Jest in watch mode, to run tests on a subset of the files.
npm run test:watch
```

## Deploying it

### Build scripts

To only build assets for either development or production you can use

- `npm run build` To build development assets
- `npm run build:prod` To build assets with minification and vendor prefixes

### Debug script

To test production, minified and vendor prefixed assets you can use

- `npm run debug` To develop with a simple http server, no browsersync and production assets

## React support

You can test that compilation of react is working by uncommenting the relevant lines in `javascript/main.js` and `javascript/components/test-react.js`. If you don't need react in your project, make sure you don't uncomment these lines or remove them completely. This will help to keep the compiled js file size down.

## Third party libraries

We no longer have a 'vendor' folder for these. Instead find ones that are packaged as npm libraries and install them as dependencies (see 'using npm' above). If they have CSS that needs including, this can be imported directly from the node_modules folder - see the example for glide in main.scss.

## CSS Background images

There is a folder inside `images` called `cssBackgrounds` where you should place any images referenced by the CSS, whether svg, jpg or png. The tooling will detect the image size, and if it is small (less than 1024 bytes), then it will be automatically encoded within the compiled CSS file. Larger images will be synced to the `cssBackgrounds` folder and referenced in the compiled CSS as a separate file. There is an example CSS file called `_test-background-images.scss` to demo this within the wagtail-kit build.

## Further details of the packages included

- **autoprefixer** - adds vendor prefixes as necessary for the browsers defined in `browserslist` in the npm config https://www.npmjs.com/package/autoprefixer
- **babel-core** - transpiler for es6 / react https://www.npmjs.com/package/babel-core
- **babel-eslint** - add-on for extra linting of experimental features (may not be necessary for all projects) https://www.npmjs.com/package/babel-eslint
- **babel-jest** - use Babel with Jest https://jestjs.io/docs/en/getting-started#using-babel
- **babel-loader** - use babel with webpack - https://www.npmjs.com/package/babel-loader
- **babel-preset-env** - babel preset for the latest version of es6, es2015
  etc. https://www.npmjs.com/package/babel-preset-env https://babeljs.io/env/
  https://babeljs.io/docs/plugins/
- **browser-sync** - for automatic reloading of your browser when changes are made to CSS / JS files https://www.npmjs.com/package/browser-sync
- **copy-webpack-plugin** - Used to sync images from static_src to static_compiled
- **css-loader** – add support for Webpack to load stylesheets.
- **cssnano** – minify CSS with safe optimisations - https://cssnano.co/.
- **eslint** - lint your javascript https://www.npmjs.com/package/eslint
- **file-loader** - Use to sync background images (larger than 1024 bytes) and fonts to the static_compiled directory, but only those that are actually used
- **jest** - testing framework for JavaScript https://jestjs.io/
- **"mini-css-extract-plugin"** - extract CSS generated by Webpack into separate files.
- **npm-run-all** - run more than one npm script concurrently - used by some of our npm scripts https://www.npmjs.com/package/npm-run-all
- **onchange** - watches for changes in a set of files - used by our watch scripts https://www.npmjs.com/package/onchange
- **postcss-cli** - required by `autoprefixer` - https://www.npmjs.com/package/postcss-cli
- **"postcss-loader"** - integrate PostCSS preprocessing into Webpack’s styles loading.
- **postcss-custom-properties** - polyfill for CSS custom properties - https://www.npmjs.com/package/postcss-custom-properties
- **stylelint** - Linting for styles - https://stylelint.io
- **stylelint-config-torchbox** - Our custom rules for linting styles
- **sass-loader** - integrate Sass preprocessing into Webpack’s styles loading.
- **url-loader** - Used to inline background images that are smaller than 1024 bytes into the CSS
- **webpack** - Bundler for js files (can do much more too) - https://www.npmjs.com/package/webpack https://webpack.js.org/concepts/
- **webpack-cli** - The webpack command calls this behind the scenese (as of webpack v 4) https://www.npmjs.com/package/webpack-cli

## React specific packages

- **babel-polyfill** - IE11 fallbacks for some js functions https://www.npmjs.com/package/babel-polyfill
- **babel-preset-react** - babel preset for react. https://www.npmjs.com/package/babel-preset-react https://babeljs.io/env/ https://babeljs.io/docs/plugins/
- **eslint-plugin-react** - linting for react and jsx https://www.npmjs.com/package/eslint-plugin-react
