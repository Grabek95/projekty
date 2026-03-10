import React, { useState } from 'react';
import axios from 'axios';

function PLKForm() {
    const [formData, setFormData] = useState({
        biz: '',
        data: '',
        data_ftth: '',
        ind: '',
        mix: '',
        miesiac: ''
    });
    const [loading, setLoading] = useState(false);
    const [message, setMessage] = useState('');

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prev => ({
            ...prev,
            [name]: value
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        setLoading(true);
        setMessage('');

        try {
            // Konwertuj miesiąc z YYYY-MM na YYYYMM
            const miesiacFormatted = formData.miesiac.replace('-', '');
            // Konwertuj na liczby (lub null jeśli puste)
            const payload = {
                biz: formData.biz ? parseInt(formData.biz) : null,
                data: formData.data ? parseInt(formData.data) : null,
                data_ftth: formData.data_ftth ? parseInt(formData.data_ftth) : null,
                ind: formData.ind ? parseInt(formData.ind) : null,
                mix: formData.mix ? parseInt(formData.mix) : null,
                miesiac: miesiacFormatted
            };

            const response = await axios.post('http://127.0.0.1:8000/api/plk/manual', payload);
            setMessage('Sukces: ' + response.data.message);

            // Wyczyść formularz po sukcesie
            setFormData({
                biz: '',
                data: '',
                data_ftth: '',
                ind: '',
                mix: ''
            });
        } catch (error) {
            setMessage('Błąd: ' + error.message);
        }
        setLoading(false);
    };

    const inputStyle = {
        width: '100%',
        padding: '8px',
        marginBottom: '10px',
        border: '1px solid #ddd',
        borderRadius: '4px',
        fontSize: '14px'
    };

    const labelStyle = {
        display: 'block',
        marginBottom: '5px',
        fontWeight: 'bold',
        color: '#333'
    };

    return (
        <div style={{ maxWidth: '500px' }}>
            <h3>Podsumowanie miesiąca PLK</h3>
            <p style={{ color: '#666', marginBottom: '20px' }}>
                Wprowadź wartości churn podsumuwujące miesiąc dla PLK.
                Wszystkie pola wymagane - puste pole zwróci błąd.
            </p>

            <form onSubmit={handleSubmit}>
                <div>
                    <label style={labelStyle}>Miesiąc</label>
                    <input
                        type="month"
                        name="miesiac"
                        value={formData.miesiac}
                        onChange={handleChange}
                        required
                        style={inputStyle}
                    />
                </div>
                <div>
                    <label style={labelStyle}>BIZ</label>
                    <input
                        type="number"
                        name="biz"
                        value={formData.biz}
                        onChange={handleChange}
                        required
                        placeholder="np. 145"
                        style={inputStyle}
                    />
                </div>

                <div>
                    <label style={labelStyle}>DATA</label>
                    <input
                        type="number"
                        name="data"
                        value={formData.data}
                        onChange={handleChange}
                        required
                        placeholder="np. 327"
                        style={inputStyle}
                    />
                </div>

                <div>
                    <label style={labelStyle}>DATA_FTTH</label>
                    <input
                        type="number"
                        name="data_ftth"
                        value={formData.data_ftth}
                        onChange={handleChange}
                        required
                        placeholder="np. 77"
                        style={inputStyle}
                    />
                </div>

                <div>
                    <label style={labelStyle}>IND</label>
                    <input
                        type="number"
                        name="ind"
                        value={formData.ind}
                        onChange={handleChange}
                        required
                        placeholder="np. 1818"
                        style={inputStyle}
                    />
                </div>

                <div>
                    <label style={labelStyle}>MIX</label>
                    <input
                        type="number"
                        name="mix"
                        value={formData.mix}
                        onChange={handleChange}
                        required
                        placeholder="np. 25"
                        style={inputStyle}
                    />
                </div>

                <button
                    type="submit"
                    disabled={loading}
                    style={{
                        padding: '12px 24px',
                        backgroundColor: loading ? '#ccc' : '#28a745',
                        color: 'white',
                        border: 'none',
                        borderRadius: '5px',
                        cursor: loading ? 'not-allowed' : 'pointer',
                        fontSize: '16px',
                        fontWeight: 'bold',
                        marginTop: '10px'
                    }}
                >
                    {loading ? 'Zapisywanie...' : 'Zapisz dane'}
                </button>
            </form>

            {message && (
                <p style={{
                    marginTop: '20px',
                    padding: '10px',
                    backgroundColor: message.includes('Sukces') ? '#d4edda' : '#f8d7da',
                    borderRadius: '5px',
                    fontWeight: 'bold'
                }}>
                    {message}
                </p>
            )}
        </div>
    );
}

export default PLKForm;