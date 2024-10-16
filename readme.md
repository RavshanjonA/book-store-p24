quyida ko'rsatilgan schema asosida projectni loyihalash.

│
├── apps/
│   ├── book/
│   │    ├── graphql/
│   │    │   ├── book/
│   │    │   │   ├── queries.py
│   │    │   │   ├── mutations.py
│   │    │   │   ├── types.py
│   │    │   │   ├── resolvers.py
│   │    │   │   └── schema.py  # (Book-specific schema)
│   │    │   ├── book_category/
│   │    │   │   ├── queries.py
│   │    │   │   ├── mutations.py
│   │    │   │   ├── types.py
│   │    │   │   ├── resolvers.py
│   │    │   │   └── schema.py  # (BookCategory-specific schema)
│   │    │   ├── book_genre/
│   │    │   │   ├── queries.py
│   │    │   │   ├── mutations.py
│   │    │   │   ├── types.py
│   │    │   │   ├── resolvers.py
│   │    │   │   └── schema.py  # (BookGenre-specific schema)
│   │    │   └── schema.py  #  Main schema combining all models

