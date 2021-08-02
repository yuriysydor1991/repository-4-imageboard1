const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: "./src/index.js",
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
    path: path.resolve(__dirname, "../src-python/myimageboard_1/views/assets/js/"),
    publicPath: "/dist/",
    filename: "react-admin-v100-bundle.js"
  },
  devServer: {
    contentBase: path.join(__dirname, "public/"),
    host: "0.0.0.0",
    port: 3000,
    //publicPath: "http://localhost:3000/dist/",
    publicPath: "/dist/",
    hotOnly: true
  },
  plugins: [new webpack.HotModuleReplacementPlugin()]
};
