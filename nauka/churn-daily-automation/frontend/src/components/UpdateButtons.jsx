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
        backgroundColor: '#28a745',
        color: 'white',
        border: 'none',
        borderRadius: '5px',
        cursor: loading ? 'not-allowed' : 'pointer',
        opacity: loading ? 0.6 : 1,
        minWidth: '250px',
        textAlign: 'center'
    };

    return (
        <div style={{
            display: 'flex',
            flexDirection: 'column',
            gap: '10px',
            alignItems: 'flex-end'
        }}>

            {/* Przyciski jedno pod drugim */}
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
                Odśwież dane
            </button>

            {/* Status messages */}
            {loading && <p style={{ margin: '5px 0', fontSize: '13px' }}>Przetwarzanie...</p>}
            {message && <p style={{ margin: '5px 0', fontWeight: 'bold', fontSize: '13px' }}>{message}</p>}
        </div>
    );
}

export default UpdateButtons;