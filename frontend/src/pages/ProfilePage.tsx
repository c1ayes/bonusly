import { ChevronRight, Gift, Settings2, CalendarDays } from "lucide-react";
import { useNavigate } from 'react-router-dom';
import { businesses } from "../data/businesses";
import { Progress } from "../components/Progress";

export default function ProfilePage() {
  const navigate = useNavigate();

  return (
    <>
      {/* Шапка профиля */}
      <header className="mb-7 flex items-center justify-between">
        <div className="flex items-center gap-3.5">
          <div className="flex h-14 w-14 items-center justify-center overflow-hidden rounded-full bg-[#e7ece9] text-lg font-semibold text-[#68736e]">
            А
          </div>
          <div>
            <h1 className="text-xl font-bold tracking-tight">Алексей</h1>
            <button className="mt-1 flex items-center gap-1 text-sm text-muted">
              Уровень: Старт <ChevronRight size={15} />
            </button>
          </div>
        </div>
        <button aria-label="Настройки" className="rounded-full p-2 text-ink hover:bg-gray-100">
          <Settings2 size={22} strokeWidth={1.7} />
        </button>
      </header>

      {/* Ближайший бонус */}
      <button className="mb-8 flex w-full items-center gap-3 rounded-2xl bg-white p-4 text-left shadow-soft">
        <span className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl bg-[#eef7f2] text-accent">
          <Gift size={22} strokeWidth={1.7} />
        </span>
        <span className="min-w-0 flex-1">
          <span className="block text-sm font-semibold">Ближайший бонус</span>
          <span className="mt-1 block text-xs text-muted">Скидка 10% через 2 посещения</span>
        </span>
        <ChevronRight size={18} className="text-muted" />
      </button>

      {/* Список бизнесов */}
      <div className="mb-4 flex items-end justify-between">
        <h2 className="text-lg font-bold tracking-tight">Мои бизнесы</h2>
        <span className="text-sm text-muted">{businesses.length}</span>
      </div>

      <div className="space-y-0">
        {businesses.map((business) => {
          const remaining = Math.max(business.target - business.visits, 0);
          
          return (
            <button
              key={business.id}
              onClick={() => navigate(`/business/${business.id}`)}
              className="group flex w-full gap-3.5 border-b border-gray-100 py-4 text-left first:pt-2 last:border-0"
            >
              <img
                src={business.image}
                alt=""
                className="h-[82px] w-[82px] shrink-0 rounded-2xl object-cover"
              />
              <span className="min-w-0 flex-1 pt-0.5">
                <span className="flex items-center justify-between gap-2">
                  <span className="truncate text-sm font-semibold">{business.name}</span>
                  <ChevronRight size={17} className="shrink-0 text-muted transition-transform group-hover:translate-x-0.5" />
                </span>
                <span className="mt-1 block text-xs text-muted">{business.category}</span>
                <span className="mt-3 mb-2 flex items-center justify-between gap-2 text-xs">
                  <span className="flex items-center gap-1.5 text-muted">
                    <CalendarDays size={14} /> {business.visits} {business.visits === 1 ? "посещение" : "посещений"}
                  </span>
                  <span className="whitespace-nowrap text-muted">До бонуса <b className="ml-1 text-ink">{remaining}</b></span>
                </span>
                <Progress value={business.visits} target={business.target} />
              </span>
            </button>
          );
        })}
      </div>
    </>
  );
}