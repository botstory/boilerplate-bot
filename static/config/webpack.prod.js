require('babel-polyfill');
var HtmlWebpackPlugin = require('html-webpack-plugin');


// Webpack config for creating the production bundle.
var path = require('path');
var webpack = require('webpack');
// var CleanPlugin = require('clean-webpack-plugin');

var projectRootPath = path.resolve(__dirname, '../');
var assetsPath = path.resolve(projectRootPath, './dist');

// https://github.com/halt-hammerzeit/webpack-isomorphic-tools
// var WebpackIsomorphicToolsPlugin = require('webpack-isomorphic-tools/plugin');
// var webpackIsomorphicToolsPlugin = new WebpackIsomorphicToolsPlugin(require('./webpack-isomorphic-tools'));

module.exports = {
  devtool: 'source-map',
  context: path.resolve(__dirname, '..'),
  entry: {
    'main': [
      // 'bootstrap-sass!./src/theme/bootstrap.config.prod.js',
      // 'font-awesome-webpack!./src/theme/font-awesome.config.prod.js',
      './src/client.js'
    ]
  },
  output: {
    path: assetsPath,
    filename: '[name]-[chunkhash].js',
    chunkFilename: '[name]-[chunkhash].js',
    publicPath: '/'
  },
  module: {
    loaders: [
      {
        test: /\.scss$/,
        loaders: ["style-loader", "css-loader", "sass-loader"]
      }
    ]
  },
  resolve: {
    modules: [
      'node_modules'
    ]
  },
  plugins: [
    new HtmlWebpackPlugin({
      template: 'src/index.html'
    })
  ]
};
