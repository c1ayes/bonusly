type ProgressProps = {
  value: number;
  target: number;
};

export function Progress({ value, target }: ProgressProps) {
  const percentage = Math.min((value / target) * 100, 100);

  return (
    <div className="h-1.5 w-full overflow-hidden rounded-full bg-gray-200">
      <div
        className="h-full rounded-full bg-accent transition-all"
        style={{ width: `${percentage}%` }}
      />
    </div>
  );
}