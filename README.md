graph TD
    %% Data Source
    A[Raw Daikibo Telemetry Data<br/>160,000+ rows JSON] --> B
    
    %% Data Engineering Phase
    subgraph ETL [Phase 1: Data Preparation Python & Pandas]
        B[Import Data] --> C[Flatten Nested Dictionaries]
        C --> D[Export Clean Relational CSV]
    end
    
    D --> E
    
    %% Data Analytics Phase
    subgraph BI [Phase 2: Visualization Tableau]
        E[Connect CSV] --> F[Create Calculated Fields]
        F --> G[Build Cross-Filtered Dashboard]
    end
    
    G --> H
    
    %% Business Value
    subgraph Insights [Phase 3: Business Insights Delivered]
        H{Bottlenecks Identified}
        H -->|Where| I[Seiko & Shenzhen Factories]
        H -->|What| J[Laser Welders & Cutters]
        H -->|When| K[Erratic Crashes May 4th-5th]
    end
    
    %% Styling
    classDef default fill:#f9f9f9,stroke:#333,stroke-width:1px;
    classDef insights fill:#e1f5fe,stroke:#0288d1,stroke-width:2px;
    class H,I,J,K insights;
