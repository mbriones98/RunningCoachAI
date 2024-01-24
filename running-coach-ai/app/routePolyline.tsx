import { MapContainer, TileLayer, Polyline, useMap } from 'react-leaflet';
import React from 'react';

export function RoutePolyline(props: { coordinates: [number, number][] }) {

    return (
        <h1>{props.coordinates}</h1>
    );
};

export default RoutePolyline;