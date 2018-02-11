import React from "react";

import Section from "../components/Section";
import Carousel from "../components/Carousel";

var axios = require('axios');

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isTilesLoaded: false,
      isCarouselLoaded: false,
      tiles: [],
      carousel: []
    };
  }
  componentDidMount() {
    axios("http://172.16.20.3:8000/dashboard")
      .then((response) => {
        this.setState({
          isTilesLoaded: true,
          tiles: response.data.results
        });
        },
        (error) => {
          this.setState({
            isTilesLoaded: true,
            error
          });
        }
      )
    axios("http://172.16.20.3:8000/dashboard/carousel")
      .then((response) => {
        this.setState({
          isCarouselLoaded: true,
          carousel: response.data.results
        });
        },
        (error) => {
          this.setState({
            isCarouselLoaded: true,
            error
          });
        }
      )
  }
  createPageContent() {
    const { tiles } = this.state;
    var num_rows = Math.ceil(tiles.length/3);
    this.rows = [];
    for (var i = 0; i < num_rows ;  i++) {
      this.rows.push(
        <div className="row big-row" key={i}>
          {tiles.map((tile, index) => {
            if (index >= 3*i && index < 3*(i+1)) {
              return <Section key={index} tiles={tile}/>;
            }
          })}
        </div>
      );
    }
  }
  render() {
    const { error, isTilesLoaded, isCarouselLoaded, carousel } = this.state;
    if (error) {
      return (
        <div>
          <p>Error: {error.message}</p>
        </div>
      );
    } else if (!isTilesLoaded || !isCarouselLoaded) {
      return (
        <div className="all-tiles l0">
          <p>Loading...</p>
        </div>
      );
    } else {
      this.createPageContent();
      return (
          <div>
            <Carousel slides={carousel}/>
            <div className="page-content-container l0">
              <div className="all-tiles">
              {this.rows.map((row, index) => {
                return row;
              })}
              </div>
            </div>
          </div>
      );
    }
  }
}
