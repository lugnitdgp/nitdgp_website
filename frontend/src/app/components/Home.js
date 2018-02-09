import React from "react";

import Section from "./Section";

var axios = require('axios');

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      tiles: []
    };
  }
  componentDidMount() {
    axios("http://172.16.20.3:8000/dashboard")
      .then((response) => {
        this.setState({
          isLoaded: true,
          tiles: response.data.results
        });
        },
        (error) => {
          this.setState({
            isLoaded: true,
            error
          });
        }
      )
  }
  render() {
    const { error, isLoaded, tiles } = this.state;
    if (error) {
      return (
        <div>
          <p>Error: {error.message}</p>
        </div>
      );
    } else if (!isLoaded) {
      return (
        <div className="all-tiles l0">
          <p>Loading...</p>
        </div>
      );
    } else {
      var num_rows = Math.ceil(tiles.length/3);
      var rows = [];
      for (var i = 0; i < num_rows ;  i++) {
        rows.push(
          <div className="row big-row">
            {tiles.map((tile, index) => {
              if (index >= 3*i && index < 3*(i+1)) {
                return <Section key={index} tiles={tile}/>;
              }
            })}
          </div>
        );
      }
      return (
        <div class="page-content-container l0">
          <div className="all-tiles">
          {rows.map((row, index) => {
            return row;
          })}
          </div>
        </div>
      );
    }
  }
}
