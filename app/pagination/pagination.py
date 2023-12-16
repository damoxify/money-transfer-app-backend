class Pagination:
    def paginate_query(self, query, page, per_page):
        """
        Paginate a SQLAlchemy query.

        :param query: SQLAlchemy query object
        :param page: Current page
        :param per_page: Number of items per page
        :return: Paginated query result
        """
        paginated_query = query.paginate(page=page, per_page=per_page, error_out=False)

        paginated_items = paginated_query.items

        result = {
            'items': paginated_items,
            'page': paginated_query.page,
            'total_pages': paginated_query.pages,
            'total_items': paginated_query.total,
        }

        return result
