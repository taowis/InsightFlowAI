from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import String, Integer, Date, JSON, Text, Numeric, BigInteger, TIMESTAMP, func, ForeignKey

Base = declarative_base()

class Client(Base):
    __tablename__ = "clients"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    brand_theme: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())

class DataSource(Base):
    __tablename__ = "data_sources"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"))
    source: Mapped[str] = mapped_column(String, nullable=False)
    credentials: Mapped[dict] = mapped_column(JSON, default=dict)
    metadata: Mapped[dict] = mapped_column(JSON, default=dict)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())

class MetricsDaily(Base):
    __tablename__ = "metrics_daily"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"))
    date: Mapped[str] = mapped_column(Date, nullable=False)
    channel: Mapped[str] = mapped_column(String, nullable=False)
    impressions: Mapped[int | None] = mapped_column(BigInteger)
    clicks: Mapped[int | None] = mapped_column(BigInteger)
    spend: Mapped[float | None] = mapped_column(Numeric(12,2))
    conversions: Mapped[int | None] = mapped_column(BigInteger)
    revenue: Mapped[float | None] = mapped_column(Numeric(12,2))
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())

class Report(Base):
    __tablename__ = "reports"
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    client_id: Mapped[int] = mapped_column(Integer, ForeignKey("clients.id"))
    period_start: Mapped[str] = mapped_column(Date, nullable=False)
    period_end: Mapped[str] = mapped_column(Date, nullable=False)
    status: Mapped[str] = mapped_column(String, default="draft")
    narrative: Mapped[str | None] = mapped_column(Text)
    file_path: Mapped[str | None] = mapped_column(String)
    created_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())
    updated_at: Mapped[str] = mapped_column(TIMESTAMP, server_default=func.now())
