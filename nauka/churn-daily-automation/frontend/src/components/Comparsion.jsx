import React, { useState, useEffect } from 'react';

function Comparison({ data }) {
    const [month1, setMonth1] = useState('');
    const [month2, setMonth2] = useState('');
    const [comparisonData, setComparisonData] = useState([]);

    // Unikalne miesiące (posortowane od najnowszego)
    const uniqueMonths = [...new Set(data.map(row => row.MIESIAC))].sort().reverse();

    // Ustaw domyślne miesiące (2 ostatnie)
    useEffect(() => {
        if (uniqueMonths.length >= 2) {
            setMonth1(uniqueMonths[1]); // Poprzedni
            setMonth2(uniqueMonths[0]); // Najnowszy
        }
    }, [data]);

    // Przygotuj dane porównawcze
    useEffect(() => {
        if (month1 && month2) {
            prepareComparison();
        }
    }, [month1, month2, data]);

    const prepareComparison = () => {
        const data1 = data.filter(row => row.MIESIAC === month1);
        const data2 = data.filter(row => row.MIESIAC === month2);

        const comparison = [];

        // Dla każdej kombinacji spółka + produkt
        const combinations = new Set();
        [...data1, ...data2].forEach(row => {
            combinations.add(`${row.SPOLKA}|${row.PRODUKT}`);
        });

        combinations.forEach(combo => {
            const [spolka, produkt] = combo.split('|');

            const val1 = data1.find(r => r.SPOLKA === spolka && r.PRODUKT === produkt)?.WARTOSC || 0;
            const val2 = data2.find(r => r.SPOLKA === spolka && r.PRODUKT === produkt)?.WARTOSC || 0;

            const change = val2 - val1;
            const changePercent = val1 !== 0 ? ((change / val1) * 100) : 0;

            comparison.push({
                spolka,
                produkt,
                val1,
                val2,
                change,
                changePercent
            });
        });

        // Sortuj po spółce i produkcie
        comparison.sort((a, b) => {
            if (a.spolka !== b.spolka) return a.spolka.localeCompare(b.spolka);
            return a.produkt.localeCompare(b.produkt);
        });

        setComparisonData(comparison);
    };

    const formatMonth = (miesiac) => {
        if (!miesiac) return '';
        return `${miesiac.substring(0, 4)}-${miesiac.substring(4, 6)}`;
    };

    // Kolor dla zmiany (churn: wzrost = dobrze = zielony, spadek = źle = czerwony)
    const getChangeColor = (change) => {
        if (change < 0) return '#dc3545'; // Zielony (spadek churn) 
        if (change > 0) return '#28a745'; // Czerwony (wzrost churn)
        return '#6c757d'; // Szary (bez zmiany)
    };

    return (
        <div>
            <h2>Porównanie miesiąc-do-miesiąca</h2>

            {/* Wybór miesięcy */}
            <div style={{
                marginBottom: '20px',
                padding: '15px',
                backgroundColor: '#f8f9fa',
                borderRadius: '5px',
                display: 'flex',
                gap: '20px',
                alignItems: 'center'
            }}>
                <div>
                    <label style={{ marginRight: '10px', fontWeight: 'bold' }}>
                        Miesiąc 1 (bazowy):
                    </label>
                    <select
                        value={month1}
                        onChange={(e) => setMonth1(e.target.value)}
                        style={{
                            padding: '8px',
                            borderRadius: '4px',
                            border: '1px solid #ddd'
                        }}
                    >
                        {uniqueMonths.map(month => (
                            <option key={month} value={month}>
                                {formatMonth(month)}
                            </option>
                        ))}
                    </select>
                </div>

                <div style={{ fontSize: '20px', fontWeight: 'bold' }}>vs</div>

                <div>
                    <label style={{ marginRight: '10px', fontWeight: 'bold' }}>
                        Miesiąc 2 (porównywany):
                    </label>
                    <select
                        value={month2}
                        onChange={(e) => setMonth2(e.target.value)}
                        style={{
                            padding: '8px',
                            borderRadius: '4px',
                            border: '1px solid #ddd'
                        }}
                    >
                        {uniqueMonths.map(month => (
                            <option key={month} value={month}>
                                {formatMonth(month)}
                            </option>
                        ))}
                    </select>
                </div>
            </div>

            {/* Tabela porównawcza */}
            {comparisonData.length > 0 ? (
                <div style={{ overflowX: 'auto' }}>
                    <table style={{
                        width: '100%',
                        borderCollapse: 'collapse',
                        marginTop: '20px'
                    }}>
                        <thead>
                            <tr style={{ backgroundColor: '#f0f0f0' }}>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>Spółka</th>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>Produkt</th>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>
                                    {formatMonth(month1)}
                                </th>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>
                                    {formatMonth(month2)}
                                </th>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>Zmiana</th>
                                <th style={{ padding: '10px', border: '1px solid #ddd' }}>Zmiana %</th>
                            </tr>
                        </thead>
                        <tbody>
                            {comparisonData.map((row, index) => (
                                <tr key={index}>
                                    <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                        {row.spolka}
                                    </td>
                                    <td style={{ padding: '8px', border: '1px solid #ddd' }}>
                                        {row.produkt}
                                    </td>
                                    <td style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'right' }}>
                                        {row.val1.toLocaleString()}
                                    </td>
                                    <td style={{ padding: '8px', border: '1px solid #ddd', textAlign: 'right' }}>
                                        {row.val2.toLocaleString()}
                                    </td>
                                    <td style={{
                                        padding: '8px',
                                        border: '1px solid #ddd',
                                        textAlign: 'right',
                                        color: getChangeColor(row.change),
                                        fontWeight: 'bold'
                                    }}>
                                        {row.change > 0 ? '+' : ''}{row.change.toLocaleString()}
                                    </td>
                                    <td style={{
                                        padding: '8px',
                                        border: '1px solid #ddd',
                                        textAlign: 'right',
                                        color: getChangeColor(row.change),
                                        fontWeight: 'bold'
                                    }}>
                                        {row.change > 0 ? '+' : ''}{row.changePercent.toFixed(1)}%
                                    </td>
                                </tr>
                            ))}
                        </tbody>
                    </table>
                </div>
            ) : (
                <p>Wybierz dwa miesiące do porównania</p>
            )}

            {/* Podsumowanie */}
            {comparisonData.length > 0 && (
                <div style={{ marginTop: '20px', padding: '15px', backgroundColor: '#f8f9fa', borderRadius: '5px' }}>
                    <h4>Podsumowanie:</h4>
                    <p>
                        Wzrost (produktów): <strong style={{ color: '#28a745' }}>
                            {comparisonData.filter(r => r.change > 0).length}
                        </strong>
                    </p>
                    <p>
                        Spadek (produktów): <strong style={{ color: '#dc3545' }}>
                            {comparisonData.filter(r => r.change < 0).length}
                        </strong>
                    </p>
                    <p>
                        Bez zmiany: <strong style={{ color: '#6c757d' }}>
                            {comparisonData.filter(r => r.change === 0).length}
                        </strong>
                    </p>
                </div>
            )}
        </div>
    );
}

export default Comparison;