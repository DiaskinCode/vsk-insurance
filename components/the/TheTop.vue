<template>
  <div class="container-wrapper bs-1">
    <div class="top container py-60 d-f ai-c jc-sb pb-40-mb pt-0-mb fd-cr-mb">
      <div class="d-f fd-c ai-fs">
        <h1 class="c-t1b fw-7 fs-35 lh-120 fs-20-mb ord-1-mb">
          Защита для вас и вашего<br class="d-n d-b-mb">
          ребенка <br class="d-n-mb">
          на случай<br class="d-n d-b-mb">
          непредвиденных событий
        </h1>
        <div class="d-f fd-c fs-22 lh-140 mt-35 row gy-30 ord-4-mb fs-20-mb mt-0-mb">
          <TopListItem>
            <h2>
              Возраст Застрахованного <span class="fw-7">от 4 до 70 лет</span>
            </h2>
          </TopListItem>
          <TopListItem>
            <h2>
              Фиксированная страховая сумма
              <br class="d-n d-b-mb">
              <span class="fw-7">
                до 1 000 000 рублей
              </span>
            </h2>
          </TopListItem>
          <TopListItem>
            <h2>
              Срок страхования <span class="fw-7"><br class="d-n d-b-mb">от 1 дня до 1 года</span>
            </h2>
          </TopListItem>
          <TopListItem class="d-n-mb">
            <h2>
              Полис
              <span class="fw-7">
                начинает действовать<br>
                в день оформления
              </span>
              договора страхования
            </h2>
          </TopListItem>
        </div>
        <a
          class="mt-40 ord-2-mb w-100-mb mt-15-mb"
          href="#calculate"
        >
          <AppButton
            class="w-100-mb"
            label="Рассчитать и оформить"
          />
        </a>
        <div class="d-n d-f-mb ord-3-mb o-50 fs-14 lh-120 mt-10">
          <div class="mr-5">
            *
          </div>
          <div>
            Полис начинает действовать в день оформления договора страхования
          </div>
        </div>
      </div>
      <div>
        <img
          class="top__img"
          src="/top.svg"
          alt="people"
        >
      </div>
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
    @media (max-width: 600px) {
      width: 24.4rem;
      height: 27.356rem;
    }
  }
}
</style>
