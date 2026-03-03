import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ChurnTable from './ChurnTable';
import UpdateButtons from './UpdateButtons';

function Dashboard() {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    // Pobierz dane z API przy załadowaniu komponentu
    useEffect(() => {
        fetchData();
    }, []);

    const fetchData = async () => {
        try {
            setLoading(true);
            const response = await axios.get('http://127.0.0.1:8000/api/churn/all');
            setData(response.data.records);
            setLoading(false);
        } catch (err) {
            setError('Błąd połączenie z API: ' + err.message)
            setLoading(false);
        }
    };

    if (loading) {
        return <div>Ładowanie danych...</div>;
    }

    if (error) {
        return <div style={{ color: 'red' }}>{error}</div>;
    }

    return (
        <div style={{ padding: '20px' }}>
            <h1>Churn Daily Dashboard</h1>
            <p>Wszystkich rekordów: {data.length}</p>

            <button
                onClick={fetchData}
                style={{
                    padding: '10px 20px',
                    backgroundColor: '#007bff',
                    color: 'white',
                    border: 'none',
                    borderRadius: '5px',
                    cursor: 'pointer'
                }}
            >
                Odśwież dane
            </button>

            <UpdateButtons />

            <ChurnTable data={data} />
        </div>
    );
}

export default Dashboard;