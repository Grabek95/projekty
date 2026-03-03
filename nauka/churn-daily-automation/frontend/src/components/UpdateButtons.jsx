import React, { useState } from 'react';
import axios from 'axios';

function UpdateButtons() {
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');

    const handleUpdateCP = async () => {
        setLoading(true);
        setMessage('');
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/update/cp');
            setMessage('Sukces: ' + response.data.message);
        } catch (error) {
            setMessage('Błąd: ' + error.message);
        }
        setLoading(false);
    };

    const handleUpdateNetia = async () => {
        setLoading(true);
        setMessage('');
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/update/netia');
            setMessage('Sukces: ' + response.data.message);
        } catch (error) {
            setMessage('Błąd: ' + error.message);
        }
        setLoading(false);
    };

    const handleRefreshAll = async () => {
        setLoading(true);
        setMessage('');
        try {
            const response = await axios.post('http://127.0.0.1:8000/api/churn_refresh/all');
            setMessage('Sukces: ' + response.data.message);
        } catch (error) {
            setMessage('Błąd: ' + error.message);
        }
        setLoading(false);
    };

    const buttonStyle = {
        padding: '10px 20px',
        margin: '5px',
        backgroundColor: '#28a745',
        color: 'white',
        border: 'none',
        borderRadius: '5px',
        cursor: loading ? 'not-allowed' : 'pointer',
        opacity: loading ? 0.6 : 1
    };

    return (
        <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '5px' }}>
            <h3>Ręczne aktualizacje</h3>

            <div style={{ marginBottom: '10px' }}>
                <button onClick={handleUpdateCP} disabled={loading} style={buttonStyle}>
                    Update CP (poprzedni miesiąc)
                </button>

                <button onClick={handleUpdateNetia} disabled={loading} style={buttonStyle}>
                    Update Netia (poprzedni miesiąc)
                </button>

                <button
                    onClick={handleRefreshAll}
                    disabled={loading}
                    style={{ ...buttonStyle, backgroundColor: '#007bff' }}
                >
                    Refresh wszystkich danych
                </button>
            </div>

            {loading && <p>Przetwarzanie...</p>}
            {message && <p style={{ marginTop: '10px', fontWeight: 'bold' }}>{message}</p>}
        </div>
    );
}

export default UpdateButtons;