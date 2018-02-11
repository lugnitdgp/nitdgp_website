import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "./views/Home";

export default class Router extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Home} />
        </Switch>
      </BrowserRouter>
    );
  }
}


module.exports = Router;
