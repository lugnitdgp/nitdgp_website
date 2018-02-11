import React from "react";

var axios = require('axios');

export default class Home extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      error: null,
      isLoaded: false,
      calendars: [],
    };
  }
  componentDidMount() {
    axios("http://172.16.20.3:8000/academics/calendar")
      .then((response) => {
        this.setState({
          isLoaded: true,
          calendars: response.data.results
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
    const { error, isLoaded, calendars } = this.state;
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
      return (
        <div class="l1 page-type-links">
          <div class="card">
            <a class="card-header white-text">Academic Calendars</a>
            <div class="card-body">
              <div class="card-text">
                <ul>
                  {calendars.map((calendar, index) => {
                    return <li key={index}><a href={calendar.file} target="new">Academic calendar for the year {calendar.year}</a></li>
                  })}
                </ul>
              </div>
            </div>
          </div>
        </div>
      );
    }
  }
}
