// bundles all javascript into one file
const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js", // entry point of javascript will be in the source directory, at index.js
  output: {
    path: path.resolve(__dirname, "./static/frontend"), // this is where the out put file will be  in static, frontend
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        exclude: /node_modules/,
        use: {
          loader: "babel-loader",
        },
      },
    ],
  },
  optimization: {
    minimize: true, // takes our javascript and makes it smallerd
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("development"),
      },
    }),
  ],
}