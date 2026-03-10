import React, { useState, useEffect } from 'react';
import axios from 'axios';
import ChurnTable from './ChurnTable';
import UpdateButtons from './UpdateButtons';
import PLKForm from './PLKForm';
import Charts from './Charts';
import { Tabs, Tab } from './Tabs';
import Comparison from './Comparsion';


function Dashboard() {
    const [data, setData] = useState([]);
    const [budget, setBudget] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedDashboardMonth, setSelectedDashboardMonth] = useState('');
    const [filterSpolka, setFilterSpolka] = useState('Wszystkie');
    const [filterMiesiac, setFilterMiesiac] = useState('Wszystkie');
    const [filterProdukt, setFilterProdukt] = useState('Wszystkie');

    // Pobierz unikalne miesiące
    const uniqueMonths = [...new Set(data.map(row => row.MIESIAC))].sort().reverse();

    // Ustaw domyślny miesiąc (najnowszy)
    useEffect(() => {
        if (uniqueMonths.length > 0 && !selectedDashboardMonth) {
            setSelectedDashboardMonth(uniqueMonths[0]);
        }
    }, [data]);

    // Formatuj miesiąc (202603 → 2026-03)
    const formatMonth = (miesiac) => {
        if (!miesiac) return '';
        return `${miesiac.substring(0, 4)}-${miesiac.substring(4, 6)}`;
    };

    // Suma dla spółki w danym miesiącu
    const getSumForMonth = (spolka, miesiac) => {
        return data
            .filter(row => row.SPOLKA === spolka && row.MIESIAC === miesiac)
            .reduce((sum, row) => sum + row.WARTOSC, 0);
    };

    // Suma wszystkich spółek w danym miesiącu
    const getTotalForMonth = (miesiac) => {
        return data
            .filter(row => row.MIESIAC === miesiac)
            .reduce((sum, row) => sum + row.WARTOSC, 0);
    };

    // Filtruj dane
    const getFilteredData = () => {
        return data.filter(row => {
            const matchSpolka = filterSpolka === 'Wszystkie' || row.SPOLKA === filterSpolka;
            const matchMiesiac = filterMiesiac === 'Wszystkie' || row.MIESIAC === filterMiesiac;
            const matchProdukt = filterProdukt === 'Wszystkie' || row.PRODUKT === filterProdukt;
            return matchSpolka && matchMiesiac && matchProdukt;
        });
    };

    // Unikalne wartości dla dropdownów
    const uniqueSpolki = ['Wszystkie', ...new Set(data.map(row => row.SPOLKA))];
    const uniqueProdukty = ['Wszystkie', ...new Set(data.map(row => row.PRODUKT))].sort();

    // Pobierz budzet dla miesiaca
    const getBudgetForProduct = (spolka, produkt, miesiac) => {
        const budgetRow = budget.find(
            row => row.ROK_MSC === miesiac &&
                row.SPOLKA === spolka &&
                row.PRODUKT === produkt
        );
        return budgetRow ? budgetRow.WARTOSC : 0;
    };

    // Przygotuj dane produktów z budżetem i wykonaniem
    const getProductsData = (miesiac) => {
        const products = [];

        // PLK - IND
        const plk_ind_execution = data
            .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'PLK' && row.PRODUKT === 'IND')
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const plk_ind_budget = getBudgetForProduct('PLK', 'IND', miesiac);
        products.push({
            produkt: 'PLK - IND',
            budget: plk_ind_budget,
            execution: plk_ind_execution,
            percent: plk_ind_budget > 0 ? ((plk_ind_execution / plk_ind_budget) * 100).toFixed(0) : 0
        });

        // PLK - MIX
        const plk_mix_execution = data
            .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'PLK' && row.PRODUKT === 'MIX')
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const plk_mix_budget = getBudgetForProduct('PLK', 'MIX', miesiac);
        products.push({
            produkt: 'PLK - MIX',
            budget: plk_mix_budget,
            execution: plk_mix_execution,
            percent: plk_mix_budget > 0 ? ((plk_mix_execution / plk_mix_budget) * 100).toFixed(0) : 0
        });

        // PLK - BIZ
        const plk_biz_execution = data
            .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'PLK' && row.PRODUKT === 'BIZ')
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const plk_biz_budget = getBudgetForProduct('PLK', 'BIZ', miesiac);
        products.push({
            produkt: 'PLK - BIZ',
            budget: plk_biz_budget,
            execution: plk_biz_execution,
            percent: plk_biz_budget > 0 ? ((plk_biz_execution / plk_biz_budget) * 100).toFixed(0) : 0
        });

        // PLK - DATA+FTTH (ZSUMOWANE!)
        const plk_data_execution = data
            .filter(row => row.MIESIAC === miesiac &&
                row.SPOLKA === 'PLK' &&
                ['DATA', 'DATA_FTTH'].includes(row.PRODUKT))
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const plk_data_budget = getBudgetForProduct('PLK', 'DATA', miesiac);
        products.push({
            produkt: 'PLK - DATA+FTTH',
            budget: plk_data_budget,
            execution: plk_data_execution,
            percent: plk_data_budget > 0 ? ((plk_data_execution / plk_data_budget) * 100).toFixed(0) : 0
        });

        // CP - TV
        const cp_tv_execution = data
            .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'CP' && row.PRODUKT === 'TV')
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const cp_tv_budget = getBudgetForProduct('CP', 'TV', miesiac);
        products.push({
            produkt: 'CP - TV',
            budget: cp_tv_budget,
            execution: cp_tv_execution,
            percent: cp_tv_budget > 0 ? ((cp_tv_execution / cp_tv_budget) * 100).toFixed(0) : 0
        });

        // CP - IN
        const cp_in_execution = data
            .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'CP' && row.PRODUKT === 'IN')
            .reduce((sum, row) => sum + row.WARTOSC, 0);
        const cp_in_budget = getBudgetForProduct('CP', 'IN', miesiac);
        products.push({
            produkt: 'CP - IN',
            budget: cp_in_budget,
            execution: cp_in_execution,
            percent: cp_in_budget > 0 ? ((cp_in_execution / cp_in_budget) * 100).toFixed(0) : 0
        });

        // NETIA - wszystkie produkty
        const netiaProducts = ['BB ONNET', 'BB OFFNET', 'TV', 'VOICE ONNET', 'VOICE OFFNET', 'MOBILE'];
        netiaProducts.forEach(prod => {
            const execution = data
                .filter(row => row.MIESIAC === miesiac && row.SPOLKA === 'NETIA' && row.PRODUKT === prod)
                .reduce((sum, row) => sum + row.WARTOSC, 0);
            const budg = getBudgetForProduct('NETIA', prod, miesiac);
            products.push({
                produkt: `NETIA - ${prod}`,
                budget: budg,
                execution: execution,
                percent: budg > 0 ? ((execution / budg) * 100).toFixed(0) : 0
            });
        });

        return products;
    };

    // Pobierz dane z API przy załadowaniu komponentu
    useEffect(() => {
        fetchData();
        fetchBudget();
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

    const fetchBudget = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/budget/all');
            setBudget(response.data.records);
        } catch (err) {
            console.error('Błąd pobierania budżetu:', err);
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
            <Tabs>
                {/* Zakładka 1: Dashboard */}
                <Tab label="Dashboard">
                    <div style={{ marginTop: '30px' }}>
                        {/* Nagłówek i dropdown obok siebie */}
                        <div style={{
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'center',
                            marginBottom: '30px'
                        }}>
                            <h3 style={{ margin: 0, fontSize: '26px', marginLeft: '20px' }}>
                                Podsumowanie danych
                            </h3>

                            {/* Łącznie - na środku */}
                            <p style={{ margin: 0, fontSize: '18px', fontWeight: 'bold', color: '#333' }}>
                                Łącznie dla {formatMonth(selectedDashboardMonth)}: <span style={{ color: '#333' }}>{getTotalForMonth(selectedDashboardMonth).toLocaleString()}</span>
                            </p>

                            <div style={{ marginRight: '20px' }}>
                                <label style={{ marginRight: '10px', fontWeight: 'bold' }}>
                                    Wybierz miesiąc:
                                </label>
                                <select
                                    value={selectedDashboardMonth}
                                    onChange={(e) => setSelectedDashboardMonth(e.target.value)}
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

                        {/* 3 KARTY Z TABELAMI WEWNĄTRZ */}
                        <div style={{
                            display: 'grid',
                            gridTemplateColumns: 'repeat(3, 1fr)',
                            gap: '20px'
                        }}>
                            {/* PLK */}
                            <div style={{
                                padding: '20px',
                                backgroundColor: '#e8f5e9',
                                border: '4px solid #00ad17',
                                borderRadius: '5px'
                            }}>
                                <h4 style={{ margin: '0 0 10px 0', color: '#00ad17', textAlign: 'center' }}>PLK</h4>
                                <p style={{ fontSize: '32px', fontWeight: 'bold', margin: '0 0 15px 0', textAlign: 'center' }}>
                                    {getSumForMonth('PLK', selectedDashboardMonth).toLocaleString()}
                                </p>

                                {/* Tabela produktów PLK */}
                                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                                    <thead>
                                        <tr style={{ backgroundColor: '#d4edda' }}>
                                            <th style={{ padding: '6px', border: '1px solid #00ad17', textAlign: 'center' }}>PRODUKT</th>
                                            <th style={{ padding: '6px', border: '1px solid #00ad17', textAlign: 'center' }}>WY</th>
                                            <th style={{ padding: '6px', border: '1px solid #00ad17', textAlign: 'center' }}>BU</th>
                                            <th style={{ padding: '6px', border: '1px solid #00ad17', textAlign: 'center' }}>%</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {getProductsData(selectedDashboardMonth)
                                            .filter(row => row.produkt.startsWith('PLK'))
                                            .map((row, index) => (
                                                <tr key={index}>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'left', fontSize: '12px' }}>
                                                        {row.produkt.replace('PLK - ', '')}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.execution.toLocaleString()}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.budget.toLocaleString()}
                                                    </td>
                                                    <td style={{
                                                        padding: '5px',
                                                        border: '1px solid #ddd',
                                                        textAlign: 'right',
                                                        fontWeight: 'bold',
                                                        color: row.percent < 70 ? '#dc3545' : row.percent < 90 ? '#ffa600' : '#28a745'
                                                    }}>
                                                        {row.percent}%
                                                    </td>
                                                </tr>
                                            ))}
                                    </tbody>
                                </table>
                            </div>

                            {/* CP */}
                            <div style={{
                                padding: '20px',
                                backgroundColor: '#fff8e1',
                                border: '4px solid #ffa600',
                                borderRadius: '5px'
                            }}>
                                <h4 style={{ margin: '0 0 10px 0', color: '#ffa600', textAlign: 'center' }}>CP</h4>
                                <p style={{ fontSize: '32px', fontWeight: 'bold', margin: '0 0 15px 0', textAlign: 'center' }}>
                                    {getSumForMonth('CP', selectedDashboardMonth).toLocaleString()}
                                </p>

                                {/* Tabela produktów CP */}
                                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                                    <thead>
                                        <tr style={{ backgroundColor: '#fff3cd' }}>
                                            <th style={{ padding: '6px', border: '1px solid #ffa600', textAlign: 'center' }}>PRODUKT</th>
                                            <th style={{ padding: '6px', border: '1px solid #ffa600', textAlign: 'center' }}>WY</th>
                                            <th style={{ padding: '6px', border: '1px solid #ffa600', textAlign: 'center' }}>BU</th>
                                            <th style={{ padding: '6px', border: '1px solid #ffa600', textAlign: 'center' }}>%</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {getProductsData(selectedDashboardMonth)
                                            .filter(row => row.produkt.startsWith('CP'))
                                            .map((row, index) => (
                                                <tr key={index}>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'left', fontSize: '12px' }}>
                                                        {row.produkt.replace('CP - ', '')}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.execution.toLocaleString()}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.budget.toLocaleString()}
                                                    </td>
                                                    <td style={{
                                                        padding: '5px',
                                                        border: '1px solid #ddd',
                                                        textAlign: 'right',
                                                        fontWeight: 'bold',
                                                        color: row.percent < 70 ? '#dc3545' : row.percent < 90 ? '#ffa600' : '#28a745'
                                                    }}>
                                                        {row.percent}%
                                                    </td>
                                                </tr>
                                            ))}
                                    </tbody>
                                </table>
                            </div>

                            {/* NETIA */}
                            <div style={{
                                padding: '20px',
                                backgroundColor: '#e3f2fd',
                                border: '4px solid #0066ff',
                                borderRadius: '5px'
                            }}>
                                <h4 style={{ margin: '0 0 10px 0', color: '#0066ff', textAlign: 'center' }}>NETIA</h4>
                                <p style={{ fontSize: '32px', fontWeight: 'bold', margin: '0 0 15px 0', textAlign: 'center' }}>
                                    {getSumForMonth('NETIA', selectedDashboardMonth).toLocaleString()}
                                </p>

                                {/* Tabela produktów NETIA */}
                                <table style={{ width: '100%', borderCollapse: 'collapse', fontSize: '13px' }}>
                                    <thead>
                                        <tr style={{ backgroundColor: '#cfe2ff' }}>
                                            <th style={{ padding: '6px', border: '1px solid #0066ff', textAlign: 'center' }}>PRODUKT</th>
                                            <th style={{ padding: '6px', border: '1px solid #0066ff', textAlign: 'center' }}>WY</th>
                                            <th style={{ padding: '6px', border: '1px solid #0066ff', textAlign: 'center' }}>BU</th>
                                            <th style={{ padding: '6px', border: '1px solid #0066ff', textAlign: 'center' }}>%</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        {getProductsData(selectedDashboardMonth)
                                            .filter(row => row.produkt.startsWith('NETIA'))
                                            .map((row, index) => (
                                                <tr key={index}>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'left', fontSize: '12px' }}>
                                                        {row.produkt.replace('NETIA - ', '')}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.execution.toLocaleString()}
                                                    </td>
                                                    <td style={{ padding: '5px', border: '1px solid #ddd', textAlign: 'right' }}>
                                                        {row.budget.toLocaleString()}
                                                    </td>
                                                    <td style={{
                                                        padding: '5px',
                                                        border: '1px solid #ddd',
                                                        textAlign: 'right',
                                                        fontWeight: 'bold',
                                                        color: row.percent < 70 ? '#dc3545' : row.percent < 90 ? '#ffa600' : '#28a745'
                                                    }}>
                                                        {row.percent}%
                                                    </td>
                                                </tr>
                                            ))}
                                    </tbody>
                                </table>
                            </div>
                        </div>

                        {/* Legenda + Aktualizacje w jednym rzędzie */}
                        <div style={{
                            marginTop: '20px',
                            display: 'flex',
                            justifyContent: 'space-between',
                            alignItems: 'flex-start',
                            gap: '5px'
                        }}>
                            {/* Legenda po lewej - wszystko w jednej linii */}
                            <div style={{
                                padding: '15px',
                                backgroundColor: '#ffffff',
                                borderRadius: '5px',
                                flex: '1',
                                display: 'flex',
                                alignItems: 'center',
                                gap: '15px'
                            }}>
                                <span style={{ fontWeight: 'bold', fontSize: '14px' }}>Legenda:</span>
                                <span style={{ fontSize: '13px' }}>
                                    <span style={{ color: '#dc3545', fontWeight: 'bold' }}>● 0-69%</span> - słabe
                                </span>
                                <span style={{ fontSize: '13px' }}>
                                    <span style={{ color: '#ffa600', fontWeight: 'bold' }}>● 70-89%</span> - średnie
                                </span>
                                <span style={{ fontSize: '13px' }}>
                                    <span style={{ color: '#28a745', fontWeight: 'bold' }}>● 90%+</span> - dobre
                                </span>
                            </div>

                            {/* Aktualizacje po prawej */}
                            <div style={{
                                display: 'flex',
                                flexDirection: 'column',
                                alignItems: 'flex-end',
                                gap: '10px'
                            }}>
                                <UpdateButtons />
                            </div>
                        </div>
                    </div>
                </Tab>

                {/* Zakładka 2: Tabela */}
                <Tab label="Tabela">
                    {/* Filtry */}
                    <div style={{
                        marginBottom: '20px',
                        padding: '15px',
                        backgroundColor: '#f8f9fa',
                        borderRadius: '5px'
                    }}>
                        <h4 style={{ marginTop: 0 }}>Filtry</h4>
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '15px' }}>
                            {/* Filtr Spółka */}
                            <div>
                                <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
                                    Spółka:
                                </label>
                                <select
                                    value={filterSpolka}
                                    onChange={(e) => setFilterSpolka(e.target.value)}
                                    style={{
                                        width: '100%',
                                        padding: '8px',
                                        borderRadius: '4px',
                                        border: '1px solid #ddd'
                                    }}
                                >
                                    {uniqueSpolki.map(spolka => (
                                        <option key={spolka} value={spolka}>{spolka}</option>
                                    ))}
                                </select>
                            </div>

                            {/* Filtr Miesiąc */}
                            <div>
                                <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
                                    Miesiąc:
                                </label>
                                <select
                                    value={filterMiesiac}
                                    onChange={(e) => setFilterMiesiac(e.target.value)}
                                    style={{
                                        width: '100%',
                                        padding: '8px',
                                        borderRadius: '4px',
                                        border: '1px solid #ddd'
                                    }}
                                >
                                    <option value="Wszystkie">Wszystkie</option>
                                    {uniqueMonths.map(month => (
                                        <option key={month} value={month}>
                                            {formatMonth(month)}
                                        </option>
                                    ))}
                                </select>
                            </div>

                            {/* Filtr Produkt */}
                            <div>
                                <label style={{ display: 'block', marginBottom: '5px', fontWeight: 'bold' }}>
                                    Produkt:
                                </label>
                                <select
                                    value={filterProdukt}
                                    onChange={(e) => setFilterProdukt(e.target.value)}
                                    style={{
                                        width: '100%',
                                        padding: '8px',
                                        borderRadius: '4px',
                                        border: '1px solid #ddd'
                                    }}
                                >
                                    {uniqueProdukty.map(produkt => (
                                        <option key={produkt} value={produkt}>{produkt}</option>
                                    ))}
                                </select>
                            </div>
                        </div>

                        {/* Przycisk Reset */}
                        <button
                            onClick={() => {
                                setFilterSpolka('Wszystkie');
                                setFilterMiesiac('Wszystkie');
                                setFilterProdukt('Wszystkie');
                            }}
                            style={{
                                marginTop: '15px',
                                padding: '8px 16px',
                                backgroundColor: '#6c757d',
                                color: 'white',
                                border: 'none',
                                borderRadius: '4px',
                                cursor: 'pointer'
                            }}
                        >
                            Wyczyść filtry
                        </button>
                    </div>

                    {/* Informacja o wynikach */}
                    <div style={{ marginBottom: '20px' }}>
                        <p>
                            Pokazuję <strong>{getFilteredData().length}</strong> z <strong>{data.length}</strong> rekordów
                        </p>
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
                            Odśwież tabelę
                        </button>
                    </div>

                    {/* Tabela z przefiltrowanymi danymi */}
                    <ChurnTable data={getFilteredData()} />
                </Tab>

                {/* Zakładka 3: Wykresy */}
                <Tab label="Wykresy">
                    <Charts data={data} />
                </Tab>

                {/* Zakładka 4: Manual PLK */}
                <Tab label="Manual PLK">
                    <PLKForm />
                </Tab>

                {/* Zakładka 5: Porównanie */}
                <Tab label="Porównanie">
                    <Comparison data={data} />
                </Tab>
            </Tabs>
        </div>
    );
}

export default Dashboard;