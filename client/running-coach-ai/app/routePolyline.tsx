'use client';
import { MapContainer, TileLayer, Polyline, useMap } from 'react-leaflet';
import React from 'react';
import 'leaflet/dist/leaflet.css'
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css'
import "leaflet-defaulticon-compatibility";

export function RoutePolyline(props: { coordinates: [number, number][] }) {
    const minX = Math.min(...props.coordinates.map(coord => coord[0]));
    const minY = Math.min(...props.coordinates.map(coord => coord[1]));
    const maxX = Math.max(...props.coordinates.map(coord => coord[0]));
    const maxY = Math.max(...props.coordinates.map(coord => coord[1]));

    return (
        <div className='map-container'>

            <MapContainer
                bounds={[[minX, minY], [maxX, maxY]]}
                scrollWheelZoom={false}
                style={{flex: 1, width: '100%'}}
            >
                <TileLayer
                    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                />
                <Polyline pathOptions={{ color: 'red' }} positions={props.coordinates} />
            </MapContainer>
        </div>

    )

    // NOTE: SVG version. Does not work, but look into later
    // const calculatedViewbox = `${minX} ${minY} ${maxX - minX} ${maxY - minY}`;

    // return (
    //     <svg viewBox={calculatedViewbox} xmlns="http://www.w3.org/2000/svg">
    //         <polyline
    //             points={props.coordinates.map(coord => `${coord[0]},${coord[1]}`).join(' ')}
    //             style={{ stroke: 'red', strokeWidth: 0.2, fill: 'none'}}
    //         />
    //     </svg>
    // );
}
        

export default RoutePolyline;