import { useEffect, useState } from "react";

type Boat = {
    id: number;
    model: string;
    manufacturer: string;
    adult_capacity: number;
    child_capacity: number;
};

function App() {
    const [boats, setBoats] = useState([]);

    useEffect(() => {
        fetch("/api/boats")
            .then((response) => response.json())
            .then((data) => setBoats(data))
            .catch((error) => console.error(error));
    }, []);

    return (
        <>
            <h1>Boats</h1>
            {boats.map((boat: Boat) => (
                <div key={boat.id}>
                    <h2>{boat.id}</h2>
                    <p>{boat.model}</p>
                    <p>{boat.manufacturer}</p>
                    <p>{boat.adult_capacity}</p>
                    <p>{boat.child_capacity}</p>
                </div>
            ))}
        </>
    );
}

export default App;
