import React from "react";
import $ from "jquery";

export default class Notices extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      count: 0,
      pages: parseInt(Math.ceil(this.props.notices.length/4))
    }
  }
  changeCount() {
    setTimeout(() => {
      this.setState({
        count: (this.state.count + 1) % this.state.pages
      });
    }, 4000);
  }
  render() {
    this.changeCount();
    const { notices } = this.props;
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"];
    return (
      <div className="news">
        <div className="card card-cascade narrower card-news">
          <div className="view gradient-card-header tile-title">
              <p className="tile-title-text">NEWSFEED</p>
          </div>

          <div className="card-body">

            {notices.map((notice, index) => {
              if (index >= this.state.count*4 && index < (this.state.count+1)*4)
              return (
                <div className="row card news-row animate-right" key={index}>
                  <div className="col date-col">
                    <div align="center" className="date-div">
                      <strong className="white-text">
                        <h4>{parseInt(notice.date.slice(-2))}</h4>
                        <h6>{months[parseInt(notice.date.slice(5, 7)) - 1]}</h6>
                      </strong>
                    </div>
                    <div className="black-text"><a href={notice.file} target="new">{notice.title}</a></div>
                  </div>
                </div>
              );
            })}

          </div>
        </div>
      </div>
    );
  }
}
