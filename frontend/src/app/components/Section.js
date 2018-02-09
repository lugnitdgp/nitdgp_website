import React from "react";

import Tile from "./Tile";

export default class Section extends React.Component {
  constructor(props) {
    super(props);
    this.num_rows = this.props.tiles.contents.map((tile) => {
      return tile.row;
    }).reduce((a,b) => {
      return Math.max(a,b)
    });
  }
  createRows() {
    this.rows = [];
    for (var i = 1 ; i <= this.num_rows ; i++) {
      this.rows.push(
        <div className="row" key={i}>
          {this.props.tiles.contents.map((tile, index) => {
            if (tile.row == i) {
              return <Tile key={index} details={tile}/>;
            }
          })}
        </div>
      );
    }
  }
  render() {
    this.createRows();
    return (
      <div className="col big-col">
        <div className={["card", "card-cascade", "narrower", "card-" + String(this.props.tiles.priority)].join(' ')}>
          <div className="view gradient-card-header tile-title">
              <p className="tile-title-text">{this.props.tiles.section_name}</p>
          </div>
          <div className="card-body text-center">
            {this.rows.map((row, index) => {
              return row;
            })}
          </div>
        </div>
      </div>
    );
  }
}
