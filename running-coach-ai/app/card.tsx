import React, { useMemo } from 'react';
import { decode } from '@googlemaps/polyline-codec';
import dynamic from 'next/dynamic';

interface CardProps {
    polyline: string;
    mileage: number;
    time: string;
}

function decodePolyline(polyline: string): [number, number][] {
    const decodedCoordinates: number[][] = decode(polyline);
    const coordinates: [number, number][] = decodedCoordinates.map(coord => [coord[0], coord[1]]);
    return coordinates;
}

const Card: React.FC<CardProps> = ({ polyline, mileage, time }) => {
    const RoutePolyline = useMemo(() => dynamic(
        () => import('./routePolyline'),
        { ssr: false }
    ), []);

    return (
        <div className="card">
            <div className="route-polyline"><RoutePolyline coordinates={decodePolyline(polyline)} /></div>
            <div className="mileage">{mileage} miles</div>
            <div className="time">{time}</div>
        </div>
    );
};

export default Card;
