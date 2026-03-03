import React from 'react';

function ChurnTable({ data }) {
    if (!data || data.length === 0) {
        return <p>Brak danych do wyświetlenia</p>;
    }

    return (
        <div style={{ overflowX: 'auto' }}>
            <table style={{
                width: '100%',
                borderCollapse: 'collapse',
                marginTop: '20px'
            }}>
                <thead>
                    <tr style={{ backgroundColor: '#f0f0f0' }}>
                        <th style={{ padding: '10px', border: '1px solid #ddd' }}>Data raportu</th>
                        <th style={{ padding: '10px', border: '1px solid #ddd' }}>Spółka</th>
                        <th style={{ padding: '10px', border: '1px solid #ddd' }}>Produkt</th>
                        <th style={{ padding: '10px', border: '1px solid #ddd' }}>Wartość</th>
                        <th style={{ padding: '10px', border: '1px solid #ddd' }}>Miesiąc</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map((row, index) => (
                        <tr key={index}>
                            <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                {row.DATA_RAPORTU}
                            </td>
                            <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                {row.SPOLKA}
                            </td>
                            <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                {row.PRODUKT}
                            </td>
                            <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                {row.WARTOSC}
                            </td>
                            <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                {row.MIESIAC}
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ChurnTable;