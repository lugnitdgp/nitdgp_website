import React from "react";
import { BrowserRouter, Route, Switch } from "react-router-dom";

import Home from "./views/Home";
import Calendar from "./views/Calendar";

export default class Router extends React.Component {
  render() {
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/academics/calendar" exact component={Calendar} />
        </Switch>
      </BrowserRouter>
    );
  }
}


module.exports = Router;
