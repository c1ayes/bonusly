import { Scissors, Sparkles, Store, Coffee } from "lucide-react";
import type { Business } from "../data/businesses";

type BusinessIconProps = {
  type: Business["icon"];
};

export function BusinessIcon({ type }: BusinessIconProps) {
  const common = { size: 17, strokeWidth: 1.8 };

  switch (type) {
    case "scissors":
      return <Scissors {...common} />;
    case "sparkles":
      return <Sparkles {...common} />;
    case "store":
      return <Store {...common} />;
    case "coffee":
    default:
      return <Coffee {...common} />;
  }
}