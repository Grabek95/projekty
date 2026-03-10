import React, { useState } from 'react';

function Tabs({ children }) {
    const [activeTab, setActiveTab] = useState(0);

    return (
        <div>
            {/* Tab Headers */}
            <div style={{
                display: 'flex',
                borderBottom: '2px solid #ddd',
                marginBottom: '20px'
            }}>
                {React.Children.map(children, (child, index) => (
                    <button
                        key={index}
                        onClick={() => setActiveTab(index)}
                        style={{
                            padding: '12px 24px',
                            border: 'none',
                            background: activeTab === index ? '#007bff' : '#f0f0f0',
                            color: activeTab === index ? 'white' : '#333',
                            cursor: 'pointer',
                            fontWeight: activeTab === index ? 'bold' : 'normal',
                            borderRadius: '5px 5px 0 0',
                            marginRight: '5px'
                        }}
                    >
                        {child.props.label}
                    </button>
                ))}
            </div>

            {/* Tab Content */}
            <div>
                {React.Children.toArray(children)[activeTab]}
            </div>
        </div>
    );
}

function Tab({ children }) {
    return <div>{children}</div>;
}

export { Tabs, Tab };