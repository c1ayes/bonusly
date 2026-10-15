export type Business = {
  id: number;
  name: string;
  category: string;
  visits: number;
  target: number;
  reward: string;
  image: string;
  icon: "scissors" | "sparkles" | "store" | "coffee";
};

export const businesses: Business[] = [
  {
    id: 1, name: "Barber House", category: "Барбершоп", visits: 3, target: 5,
    reward: "Скидка 10%", image: "https://images.unsplash.com/photo-1503951914875-452162b0f3f1?auto=format&fit=crop&w=240&q=80",
    icon: "scissors"
  },
  {
    id: 2, name: "Beauty Lab", category: "Салон красоты", visits: 5, target: 6,
    reward: "Бесплатная укладка",
    image: "https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=240&q=80",
    icon: "sparkles"
  },
  {
    id: 3, name: "Urban Store", category: "Магазин", visits: 1, target: 5,
    reward: "Бонус 500 ₸",
    image: "https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=240&q=80",
    icon: "store"
  },
  {
    id: 4, name: "Coffee Point", category: "Кофейня", visits: 2, target: 5,
    reward: "Бесплатный напиток",
    image: "https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?auto=format&fit=crop&w=240&q=80",
    icon: "coffee"
  }
];