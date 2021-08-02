const path = require("path");
const webpack = require("webpack");

console.log(path.resolve(__dirname, "../src-python/myimageboard_1/views/assets/js/"))

module.exports = {
  entry: "./src-webpack/index.js",
  mode: "development",
  module: {
    rules: [
      {
        test: /\.(js|jsx)$/,
        exclude: /(node_modules|bower_components)/,
        loader: "babel-loader",
        options: { presets: ["@babel/env"] }
      },
      {
        test: /\.css$/,
        use: ["style-loader", "css-loader"]
      }
    ]
  },
  resolve: { extensions: ["*", ".js", ".jsx"] },
  output: {
    path: path.resolve(__dirname, "src-python/myimageboard_1/views/assets/js/"),
    publicPath: "/assets/js/",
    filename: "bundle.js"
  },
  devServer: {
    contentBase: path.join(__dirname, "public/"),
    host: "0.0.0.0",
    port: 3000,
    //publicPath: "http://localhost:3000/dist/",
    publicPath: "/dist/",
    hotOnly: true
  },
  plugins: [new webpack.HotModuleReplacementPlugin()],
  /* optimization: {
    minimizer: [new UglifyJsPlugin()],
  }, */
};
