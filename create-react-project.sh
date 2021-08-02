#!/bin/bash

npm init 

npm install react react-dom react-admin react-bootstrap bootstrap jquery

npm install --save-dev  @babel/core @babel/cli @babel/preset-env @babel/preset-react webpack webpack-cli webpack-dev-server style-loader css-loader babel-loader @fortawesome/fontawesome-svg-core @fortawesome/free-solid-svg-icons @fortawesome/react-fontawesome ra-data-json-server

echo '{ 
  "presets": ["@babel/env", "@babel/preset-react"]
}' > .babelrc

mkdir -v public src 

echo 'const path = require("path");
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
    path: path.resolve(__dirname, "dist/"),
    publicPath: "/dist/",
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
  plugins: [new webpack.HotModuleReplacementPlugin()]
};' > webpack.config.js

echo '<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>React Starter</title>
</head>

<body>
  <div id="root"></div>
  <noscript>
    You need to enable JavaScript to run this app.
  </noscript>
  <script src="../dist/bundle.js"></script>
</body>

</html>' > public/index.html

echo 'import React from "react";
import ReactDOM from "react-dom";
import App from "./App.js";
ReactDOM.render(<App />, document.getElementById("root"));
' > src/index.js

echo 'import React, { Component} from "react";
import Button from "react-bootstrap/Button";
import Jumbotron from "react-bootstrap/Jumbotron";
import Toast from "react-bootstrap/Toast";
import Container from "react-bootstrap/Container";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";

class App extends Component{
  render(){
    return(
      <Container fluid>
        <h1>Hello, World!</h1>
        <Button className="btn btn-lg btn-success">Bootstrap button</Button>
      </Container>
    );
  }
}

export default App;' > src/App.js

echo '.App 
{
  margin: 1rem;
  font-family: Arial, Helvetica, sans-serif;
}' > src/App.css

exit 0

echo "Creating python3 venv\n\n"

mkdir -v python-env
export VENV=$(realpath ./)
echo "VENV env variable points to "$VENV
sudo apt-get install python3.8-venv
python3 -m venv $VENV
$VENV/bin/pip install --upgrade pip setuptools
$VENV/bin/pip install pyramid==2.0 waitress pyramid_debugtoolbar
$VENV/bin/pip install mysql-connector-python
