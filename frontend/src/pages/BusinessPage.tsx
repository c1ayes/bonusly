import { useParams, useNavigate } from "react-router-dom";
import { ArrowLeft, CalendarDays, Check, ChevronRight, Gift, MapPin, Scissors } from "lucide-react";
import { businesses } from "../data/businesses";
import { visits } from "../data/visits";
import { Progress } from "../components/Progress";
import { BusinessIcon } from "../components/BusinessIcon";

export default function BusinessPage() {
  const { id } = useParams<{ id: string }>();
  const navigate = useNavigate();

  // Находим нужный бизнес по ID из URL (или берем первый по умолчанию)
  const business = businesses.find((b) => b.id === Number(id)) || businesses[0];
  const remaining = Math.max(business.target - business.visits, 0);

  return (
    <>
      {/* Кнопка назад */}
      <button 
        onClick={() => navigate("/")} 
        className="mb-5 inline-flex items-center gap-2 py-1 text-sm font-medium text-ink hover:opacity-80"
      >
        <ArrowLeft size={19} /> Назад
      </button>

      {/* Баннер с изображением */}
      <div className="relative mb-5 h-52 overflow-hidden rounded-3xl bg-gray-200">
        <img src={business.image} alt={business.name} className="h-full w-full object-cover" />
        <div className="absolute inset-0 bg-gradient-to-t from-black/40 via-transparent to-transparent" />
        <div className="absolute bottom-4 left-4 flex items-center gap-2 rounded-full bg-white/95 px-3 py-2 text-xs font-medium text-ink shadow-sm">
          <BusinessIcon type={business.icon} /> Партнёр программы
        </div>
      </div>

      {/* Шапка с информацией */}
      <div className="mb-6">
        <h1 className="text-2xl font-bold tracking-tight">{business.name}</h1>
        <p className="mt-1 text-sm text-muted">{business.category}</p>
        <div className="mt-4 flex items-center justify-between text-sm">
          <span className="flex items-center gap-2 text-muted">
            <MapPin size={17} /> ул. Ленина, 12
          </span>
          <span className="text-muted">5 мин пешком</span>
        </div>
      </div>

      {/* Прогресс посещений */}
      <section className="mb-7 rounded-2xl bg-white p-5 shadow-soft">
        <div className="mb-4 flex items-center justify-between gap-3">
          <div className="flex items-center gap-2.5">
            <CalendarDays size={21} strokeWidth={1.7} />
            <span className="text-sm font-medium">{business.visits} посещения</span>
          </div>
          <span className="text-xs text-muted">
            До бонуса <b className="ml-1 text-sm text-ink">{remaining}</b>
          </span>
        </div>
        <Progress value={business.visits} target={business.target} />
        <p className="mt-3 text-xs text-muted">
          {business.visits} из {business.target} посещений до награды
        </p>
      </section>

      {/* Ближайший бонус */}
      <section className="mb-7">
        <h2 className="mb-3 text-base font-bold">Ближайший бонус</h2>
        <div className="flex items-center gap-3 rounded-2xl bg-[#edf7f1] p-4">
          <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-full bg-white text-accent shadow-sm">
            <Gift size={21} strokeWidth={1.7} />
          </span>
          <div className="min-w-0 flex-1">
            <p className="text-sm font-semibold">{business.reward}</p>
            <p className="mt-1 text-xs text-muted">
              {remaining > 0 ? `Через ${remaining} ${remaining === 1 ? "посещение" : "посещения"}` : "Бонус доступен"}
            </p>
          </div>
          <ChevronRight size={18} className="text-muted" />
        </div>
      </section>

      {/* История посещений */}
      <section className="pb-6">
        <div className="mb-2 flex items-center justify-between">
          <h2 className="text-base font-bold">История посещений</h2>
          <button className="text-xs font-medium text-accent">Все</button>
        </div>
        <div className="divide-y divide-gray-100 rounded-2xl bg-white px-4 shadow-soft">
          {visits.map((visit) => (
            <div key={visit.date} className="flex items-center gap-3 py-4">
              <span className="flex h-10 w-10 shrink-0 items-center justify-center rounded-xl bg-gray-50 text-muted">
                <Scissors size={18} strokeWidth={1.7} />
              </span>
              <div className="min-w-0 flex-1">
                <p className="text-sm font-medium">{visit.service}</p>
                <p className="mt-1 text-xs text-muted">{visit.date}</p>
              </div>
              <div className="text-right">
                <p className="text-sm font-semibold">{visit.price}</p>
                <p className="mt-1 flex items-center justify-end gap-1 text-xs text-accent">
                  <Check size={13} /> Учтено
                </p>
              </div>
            </div>
          ))}
        </div>
      </section>
    </>
  );
}