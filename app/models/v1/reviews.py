import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.v1.base import BaseModel

if TYPE_CHECKING:
    from app.models.v1.users import UserModel
    from app.models.v1.cars import CarModel
    from app.models.v1.rentals import RentalModel

class ReviewModel(BaseModel):
    """
    Модель отзыва клиента.

    Содержит информацию об отзывах пользователей об автомобилях или сервисе,
    включая оценку, комментарий и дату создания.

    Attributes:
        id: UUID идентификатор отзыва
        user_id: UUID пользователя, оставившего отзыв
        car_id: UUID автомобиля, к которому относится отзыв (опционально)
        rental_id: UUID аренды, к которой относится отзыв (опционально)
        rating: Оценка (от 1 до 5)
        comment: Текст отзыва (опционально)
        created_at: Дата и время создания отзыва
    """

    __tablename__ = "reviews"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, nullable=False
    )
    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("users.id"), nullable=False
    )
    car_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("cars.id"), nullable=True
    )
    rental_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("rentals.id"), nullable=True
    )
    rating: Mapped[int] = mapped_column(Integer, nullable=False)
    comment: Mapped[str] = mapped_column(Text, nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )

    # Связи
    user: Mapped["UserModel"] = relationship(back_populates="reviews")
    car: Mapped["CarModel"] = relationship()
    rental: Mapped["RentalModel"] = relationship(back_populates="reviews")