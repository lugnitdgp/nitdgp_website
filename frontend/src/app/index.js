import React from "react";
import ReactDOM from "react-dom";

import "bootstrap";

import Home from "./components/Home";
import Header from "./components/Header";
import Footer from "./components/Footer";

const header = document.getElementById('header');
const pageContent = document.getElementsByClassName('page-content-container')[0];
const footer = document.getElementById('footer');

ReactDOM.render(<Header/>, header);
ReactDOM.render(<Home/>, pageContent);
ReactDOM.render(<Footer/>, footer);
