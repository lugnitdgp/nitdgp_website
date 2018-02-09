import React from "react";

export default class Tile extends React.Component {
  render() {
    return (
      <div className="col tile-small">
        <a href={this.props.details.link}>
          <div align="center" className="tile-content">
            <i className={["fa", "fa-2x", this.props.details.icon].join(' ')}></i>
            <br/>
            <p className="tile-small-text">{this.props.details.name}</p>
          </div>
        </a>
      </div>
    );
  }
}
