<template>
  <div class="top container py-60 d-f ai-c jc-sb bs-1">
    <div class="d-f fd-c ai-fs">
      <h1 class="c-t1b fw-7 fs-35 lh-120">
        Защита для вас и вашего ребенка<br>
        на случай непредвиденных событий
      </h1>
      <div class="d-f fd-c fs-22 lh-140 mt-35 row gy-30">
        <TopListItem>
          <h2>
            Возраст Застрахованного <span class="fw-7">от 4 до 70 лет</span>
          </h2>
        </TopListItem>
        <TopListItem>
          <h2>
            Фиксированная страховая сумма <span class="fw-7">200 000 рублей</span>
          </h2>
        </TopListItem>
        <TopListItem>
          <h2>
            Срок страхования <span class="fw-7">от 1 дня до 1 года</span>
          </h2>
        </TopListItem>
        <TopListItem>
          <h2>
            Полис
            <span class="fw-7">
              начинает действовать<br>
              на следующий день
            </span>
            после оформления
          </h2>
        </TopListItem>
      </div>
      <AppButton
        class="mt-40"
        label="Рассчитать и оформить"
      />
    </div>
    <div>
      <img
        class="top__img"
        src="/top.svg"
        alt="people"
      >
    </div>
  </div>
</template>

<script>
export default {
  name: '',
  props: {},
  data: () => ({
  }),
  computed: {},
  methods: {},
}
</script>

<style lang="scss">
.top {
  /* .top__item */
  &__item {
    &::before {
      content: url('/check.svg');
      width: 1.75rem;
      height: 1.153rem;
    }
  }
  /* .top__img */
  &__img {
    width: 47.4rem;
    height: 53.141rem;
  }
}
</style>
