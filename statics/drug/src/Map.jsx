import React, { Component } from 'react';

import { withGoogleMap, GoogleMap, Marker } from "react-google-maps";
import PropTypes from 'prop-types';



const MyMap = withGoogleMap(props => {

  return (
    <GoogleMap
      defaultZoom={4}
      defaultCenter={{ lat: 40.0412204, lng: -100.9387545 }}
    >
    </GoogleMap >
  )
}
);

class Map extends Component {
  render() {
    return (
      <div>
        <MyMap
          containerElement={
            <div style={{ height: `1000px` }} />
          }
          mapElement={
            <div style={{ height: `1000px` }} />
          }
        ></MyMap>
      </div>)
  }
}


export default Map;
