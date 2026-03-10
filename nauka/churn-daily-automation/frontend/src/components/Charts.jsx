import React, { useState, useEffect } from 'react';
import { LineChart, Line, BarChart, Bar, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer } from 'recharts';

function Charts({ data }) {
    const [chartData, setChartData] = useState([]);
    const [selectedMonth, setSelectedMonth] = useState('');
    const [monthlyData, setMonthlyData] = useState([]);

    // eslint-disable-next-line react-hooks/exhaustive-deps
    useEffect(() => {
        if (data && data.length > 0) {
            prepareChartData();
            prepareMonthlyComparison();
        }
    }, [data]);

    // Przygotuj dane do wykresu liniowego (trendy)
    const prepareChartData = () => {
        // Grupuj po miesiącu i spółce
        const grouped = {};

        data.forEach(row => {
            const miesiac = row.MIESIAC;
            if (!grouped[miesiac]) {
                grouped[miesiac] = { miesiac, PLK: 0, CP: 0, NETIA: 0 };
            }
            grouped[miesiac][row.SPOLKA] += row.WARTOSC;
        });

        // Konwertuj na array i sortuj po miesiącu
        const result = Object.values(grouped).sort((a, b) =>
            a.miesiac.localeCompare(b.miesiac)
        );

        setChartData(result);

        // Ustaw najnowszy miesiąc jako domyślny
        if (result.length > 0) {
            setSelectedMonth(result[result.length - 1].miesiac);
        }
    };

    // Przygotuj dane do wykresu słupkowego (porównanie spółek)
    const prepareMonthlyComparison = () => {
        if (!selectedMonth) return;

        const monthData = data.filter(row => row.MIESIAC === selectedMonth);

        // Grupuj po spółce
        const grouped = {};
        monthData.forEach(row => {
            if (!grouped[row.SPOLKA]) {
                grouped[row.SPOLKA] = 0;
            }
            grouped[row.SPOLKA] += row.WARTOSC;
        });

        const result = Object.keys(grouped).map(spolka => ({
            spolka,
            wartosc: grouped[spolka]
        }));

        setMonthlyData(result);
    };

    // eslint-disable-next-line react-hooks/exhaustive-deps
    useEffect(() => {
        prepareMonthlyComparison();
    }, [selectedMonth]);

    // Pobierz unikalne miesiące do dropdownu
    const uniqueMonths = [...new Set(data.map(row => row.MIESIAC))].sort();

    // Formatuj miesiąc dla wyświetlenia (202603 → 2026-03)
    const formatMonth = (miesiac) => {
        return `${miesiac.substring(0, 4)}-${miesiac.substring(4, 6)}`;
    };

    return (
        <div>
            <h2>Wykresy</h2>

            {/* Wykres liniowy - trendy */}
            <div style={{ marginBottom: '40px' }}>
                <h3>Trendy w czasie (suma dla każdej spółki)</h3>
                <ResponsiveContainer width="100%" height={400}>
                    <LineChart data={chartData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis
                            dataKey="miesiac"
                            tickFormatter={formatMonth}
                        />
                        <YAxis />
                        <Tooltip
                            labelFormatter={formatMonth}
                        />
                        <Legend />
                        <Line type="monotone" dataKey="PLK" stroke="#00ad17" strokeWidth={2} />
                        <Line type="monotone" dataKey="CP" stroke="#ffa600" strokeWidth={2} />
                        <Line type="monotone" dataKey="NETIA" stroke="#0066ff" strokeWidth={2} />
                    </LineChart>
                </ResponsiveContainer>
            </div>

            {/* Wykres słupkowy - porównanie */}
            <div>
                <h3>Porównanie spółek</h3>
                <div style={{ marginBottom: '20px' }}>
                    <label style={{ marginRight: '10px', fontWeight: 'bold' }}>
                        Wybierz miesiąc:
                    </label>
                    <select
                        value={selectedMonth}
                        onChange={(e) => setSelectedMonth(e.target.value)}
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

                <ResponsiveContainer width="100%" height={400}>
                    <BarChart data={monthlyData}>
                        <CartesianGrid strokeDasharray="3 3" />
                        <XAxis dataKey="spolka" />
                        <YAxis />
                        <Tooltip />
                        <Legend />
                        <Bar dataKey="wartosc" fill="#467381" />
                    </BarChart>
                </ResponsiveContainer>
            </div>
        </div>
    );
}

export default Charts;