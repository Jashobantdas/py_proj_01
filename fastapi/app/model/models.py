from datetime import date

from configs.database import engine
from sqlalchemy import Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship, DeclarativeBase


class Base(DeclarativeBase):
    pass

class Department(Base):
    __tablename__ = "department"

    id: Mapped[int] = mapped_column("d_id",Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column("d_name",String, nullable=False)
    employees: Mapped[list["Employee"]] = relationship("Employee", back_populates="department",lazy="noload")

    def __repr__(self):
        return f"Department(id={self.id}, name={self.name}, employees={self.employees})"

class Employee(Base):
    __tablename__ = 'employee'

    id: Mapped[int] = mapped_column("e_id", Integer, primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column("e_name", String, nullable=False)
    salary: Mapped[float] = mapped_column("e_salary", Float, nullable=False)
    d_id: Mapped[int] = mapped_column("e_dept",ForeignKey("department.d_id"))
    department: Mapped["Department"] = relationship(back_populates="employees",lazy="noload")

    def __repr__(self):
        return f"Employee(id={self.id}, name={self.name}, salary={self.salary}, d_id={self.d_id}, department={self.department})"

class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column("u_id", Integer, primary_key=True, autoincrement=True, nullable=False)
    first_name: Mapped[str] = mapped_column("first_name", String, nullable=False)
    last_name: Mapped[str] = mapped_column("last_name", String, nullable=False)
    u_name: Mapped[str] = mapped_column("u_name", String, nullable=False)
    email: Mapped[str] = mapped_column("email", String, nullable=False, unique=True)
    password: Mapped[str] = mapped_column("password", String, nullable=False)
    role: Mapped[str] = mapped_column("role", String, nullable=False)
    last_login: Mapped[str] = mapped_column("last_login", String, nullable=False)

    def __repr__(self):
        return f"User(id:{self.id}, name:{self.u_name},u_name:{self.u_name}, email:{self.email}, role:{self.role}, last_login:{self.last_login})"

class RagDocuments(Base):
    __tablename__ = 'rag_documents'

    document_id: Mapped[int] = mapped_column("r_id", Integer, primary_key=True, autoincrement=True, nullable=False)
    tenant_id: Mapped[int] = mapped_column("tenant_id", Integer, primary_key=True, autoincrement=True, nullable=False)
    file_name: Mapped[str] = mapped_column("f_name", String, primary_key=True, autoincrement=True, nullable=False)
    document_type: Mapped[str] = mapped_column("d_type", String, primary_key=True, autoincrement=True, nullable=False)
    storage_path: Mapped[str] = mapped_column("d_path", String, primary_key=True, autoincrement=True, nullable=False)
    status: Mapped[str] = mapped_column("r_id", String, primary_key=True, autoincrement=True, nullable=False)
    created_at: Mapped[date] = mapped_column("created_at", Date, primary_key=True, autoincrement=True, nullable=False)

    def __repr__(self) -> str:
        return f"Document( document_id={self.document_id}, tenant_id={self.tenant_id}, file_name={self.file_name}, document_type={self.document_type}, storage_path={self.storage_path}, status={self.status}, created_at={self.created_at})>"

Base.metadata.create_all(bind=engine)